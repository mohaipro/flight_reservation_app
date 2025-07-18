import tkinter as tk
from tkinter import messagebox
import database

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Book a Flight", font=("Arial", 20, "bold")).pack(pady=20)

        self.entries = {}
        fields = [
            ("Passenger Name", "name"),
            ("Flight Number", "flight_number"),
            ("Departure", "departure"),
            ("Destination", "destination"),
            ("Date (YYYY-MM-DD)", "date"),
            ("Seat Number", "seat_number")
        ]

        for label_text, field_key in fields:
            frame = tk.Frame(self)
            frame.pack(pady=5)
            tk.Label(frame, text=label_text, width=20, anchor='w').pack(side="left")
            entry = tk.Entry(frame, width=30)
            entry.pack(side="left")
            self.entries[field_key] = entry

        tk.Button(self, text="Submit Reservation", font=("Arial", 12), bg="#4CAF50", fg="white", width=20,
                  command=self.submit_form).pack(pady=20)

        tk.Button(self, text="Back to Home", font=("Arial", 12), bg="#f44336", fg="white", width=20,
                  command=lambda: controller.show_frame("HomePage")).pack(pady=5)

    def submit_form(self):
        data = {key: entry.get().strip() for key, entry in self.entries.items()}
        if any(value == "" for value in data.values()):
            messagebox.showerror("Input Error", "Please fill out all fields.")
            return
        try:
            database.add_reservation(data)
            messagebox.showinfo("Success", "Reservation submitted successfully!")
            for entry in self.entries.values():
                entry.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")