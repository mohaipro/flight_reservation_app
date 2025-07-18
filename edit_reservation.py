import tkinter as tk
from tkinter import messagebox
import database

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Edit Reservation", font=("Arial", 20, "bold")).pack(pady=20)

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

        tk.Button(self, text="Update Reservation", font=("Arial", 12), bg="#4CAF50", fg="white", width=20,
                  command=self.update_reservation).pack(pady=20)

        tk.Button(self, text="Back to Home", font=("Arial", 12), bg="#f44336", fg="white", width=20,
                  command=lambda: controller.show_frame("HomePage")).pack(pady=5)

    def load_data(self, reservation_data):
        self.current_id = reservation_data.get("id")
        for key, entry in self.entries.items():
            entry.delete(0, tk.END)
            entry.insert(0, reservation_data.get(key, ""))

    def update_reservation(self):
        new_data = {key: entry.get().strip() for key, entry in self.entries.items()}
        if any(value == "" for value in new_data.values()):
            messagebox.showerror("Error", "Please fill in all fields before updating.")
            return
        database.update_reservation(self.current_id, new_data)
        messagebox.showinfo("Updated", "Reservation updated successfully!")