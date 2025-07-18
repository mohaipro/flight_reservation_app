# ✈️ Flight Reservation Desktop App

A simple desktop application for managing flight reservations built using **Python**, **Tkinter**, and **SQLite**.

## 📋 Features

- GUI-based interface with multiple pages
- Book a new flight reservation
- View all reservations in a table
- Edit and delete existing reservations
- Data stored locally using SQLite
- Easy-to-use navigation and layout

## 🛠 Technologies Used

- Python 3
- Tkinter (for GUI)
- SQLite (for local database)
- Object-Oriented Programming (OOP)

## 🗂 Project Structure
flight_reservation_app/
├── main.py
├── booking.py
├── home.py
├── reservations.py
├── edit_reservation.py
├── database.py
├── flights.db (auto-created)
├── requirements.txt
└── README.md

## ▶️ How to Run the App

1. **Clone or Download** the project
2. Make sure you have **Python 3** installed
3. Install any required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. (Optional) Initialize the database if not already created:
    ```bash
    python -c "import database; database.create_table()"
    ```
5. Run the application:
    ```bash
    python main.py
    ```

## 📦 Packaging (Optional)

To convert to `.exe` for Windows:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
