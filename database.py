import sqlite3

DB_NAME = "flights.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_reservation(data):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["name"], data["flight_number"], data["departure"],
        data["destination"], data["date"], data["seat_number"]
    ))
    conn.commit()
    conn.close()

def get_all_reservations():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    results = cursor.fetchall()
    conn.close()
    return results

def delete_reservation(reservation_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
    conn.commit()
    conn.close()

def update_reservation(reservation_id, new_data):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE reservations SET
            name = ?, flight_number = ?, departure = ?,
            destination = ?, date = ?, seat_number = ?
        WHERE id = ?
    """, (
        new_data["name"], new_data["flight_number"], new_data["departure"],
        new_data["destination"], new_data["date"], new_data["seat_number"],
        reservation_id
    ))
    conn.commit()
    conn.close()