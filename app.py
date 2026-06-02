import sqlite3
import requests
from flask import Flask, request, redirect, render_template, g

app = Flask(__name__)
DATABASE = "orders.db"

# ☕ UPDATED COFFEE MENU (artırıldı)
PRICES = {
    "Espresso": 2.50,
    "Latte": 3.50,
    "Mocha": 4.00,
    "Iced Coffee": 3.00,
    "Americano": 2.80,
    "Cappuccino": 3.60,
    "Flat White": 3.80,
    "Macchiato": 3.20,
    "Cold Brew": 4.20,
    "Frappé": 4.50
}

# ---------- WEATHER ----------
def get_weather(city="Baku"):
    api_key = "f9ce84cf4488893701652992bb26fb8c"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    res = requests.get(url)
    data = res.json()

    # SAFE CHECK (crash olmasın deyə)
    if res.status_code != 200:
        return 20, "Clear"

    temp = data["main"]["temp"]
    weather = data["weather"][0]["main"]

    return temp, weather


# ---------- AI RECOMMENDER ----------
def recommend_coffee(temp, weather):
    weather = weather.lower()

    if "rain" in weather or "cloud" in weather:
        return ["Latte", "Mocha", "Flat White"]

    if temp <= 10:
        return ["Espresso", "Macchiato", "Flat White"]

    if temp >= 25:
        return ["Iced Coffee", "Cold Brew", "Frappé"]

    return ["Latte", "Flat White", "Mocha", "Espresso"]


# ---------- DATABASE ----------
def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db:
        db.close()


def init_db():
    db = sqlite3.connect(DATABASE)
    db.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            drink TEXT NOT NULL,
            price REAL NOT NULL,
            notes TEXT
        )
    """)
    db.commit()
    db.close()


# ---------- ROUTES ----------
@app.route("/")
def home():
    db = get_db()
    count = db.execute("SELECT COUNT(*) FROM orders").fetchone()[0]

    # weather + recommendation
    temp, weather = get_weather()
    suggestions = recommend_coffee(temp, weather)

    return render_template(
        "index.html",
        order_count=count,
        temp=temp,
        weather=weather,
        suggestions=suggestions
    )


@app.route("/order", methods=["POST"])
def place_order():
    name = request.form.get("name")
    drink = request.form.get("drink")
    notes = request.form.get("notes")

    if name and drink:
        price = PRICES.get(drink, 3.0)

        db = get_db()
        db.execute(
            "INSERT INTO orders (name, drink, price, notes) VALUES (?, ?, ?, ?)",
            (name, drink, price, notes)
        )
        db.commit()

    return redirect("/orders")


@app.route("/orders")
def show_orders():
    db = get_db()
    orders = db.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()

    total_orders = len(orders)
    total_revenue = sum(o["price"] for o in orders)

    return render_template(
        "orders.html",
        orders=orders,
        total_orders=total_orders,
        total_revenue=total_revenue
    )


@app.route("/delete/<int:order_id>", methods=["POST"])
def delete_order(order_id):
    db = get_db()
    db.execute("DELETE FROM orders WHERE id=?", (order_id,))
    db.commit()
    return redirect("/orders")


if __name__ == "__main__":
    init_db()
    app.run(debug=True, port=5001)