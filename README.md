# ☕ Bean & Brew — Coffee Shop Website

**Project by Cavid and Ibad**

A simple **full-stack web application** for a coffee shop. The frontend is built with
**HTML & CSS**, and the backend is built with **Python (Flask)** using a **SQLite**
database to store customer orders.

---

## ✨ Features

- 🏠 **Landing page** — navbar, hero banner, menu, testimonials and about sections
- 📝 **Order form** — customers can order a drink (saved to the database)
- 📋 **Orders page** — shows every order placed, in a clean table
- 📊 **Live statistics** — total number of orders and total revenue (calculated in Python)
- 🗑️ **Delete orders** — remove any order with one click
- 💾 **SQLite database** — orders are saved permanently, even after restart
- 📱 **Responsive design** — works on phones and computers

---

## 🛠️ Technologies Used

| Part      | Technology        |
|-----------|-------------------|
| Frontend  | HTML, CSS         |
| Backend   | Python (Flask)    |
| Database  | SQLite            |
| Templates | Jinja2            |

---

## 📁 Project Structure

```
temp/
├── app.py              → Python backend (the server logic)
├── requirements.txt    → list of Python libraries needed
├── README.md           → this file
├── orders.db           → database file (created automatically)
├── templates/
│   ├── index.html      → main website page + order form
│   └── orders.html     → page that lists all orders + statistics
└── static/
    └── style.css       → all the styling
```

---

## ▶️ How to Run

1. **Create a virtual environment** and install the requirements:
   ```bash
   python3 -m venv venv
   source venv/bin/activate          # Mac/Linux
   venv\Scripts\activate             # Windows
   pip install -r requirements.txt
   ```

2. **Start the server:**
   ```bash
   python app.py
   ```

3. **Open your browser** at:
   ```
   http://127.0.0.1:5001
   ```

> To stop the server, press `CTRL + C` in the terminal.

---

## 🔗 Pages & Routes

| Route             | Method | What it does                          |
|-------------------|--------|---------------------------------------|
| `/`               | GET    | Show the main website                 |
| `/order`          | POST   | Save a new order to the database      |
| `/orders`         | GET    | Show all orders + statistics          |
| `/delete/<id>`    | POST   | Delete one order by its id            |

---

## 💡 How It Works (for the presentation)

1. **Frontend (HTML/CSS):** builds the structure and look of the page.
2. **Order form:** when submitted, it sends the data to the Python backend (POST request).
3. **Flask backend:** receives the data, calculates the price, and saves it to the database.
4. **SQLite database:** stores all orders permanently in `orders.db`.
5. **Jinja templates:** Python sends data into the HTML (order list, stats, counts).
6. **CRUD operations:** the app can **C**reate (place order), **R**ead (view orders),
   and **D**elete orders — the core idea behind most real applications.

---

## 👤 Author

Made by **Cavid and Ibad**.
