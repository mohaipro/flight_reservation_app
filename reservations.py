import tkinter as tk
from tkinter import messagebox
import database

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="All Reservations", font=("Arial", 20, "bold")).pack(pady=20)

        headers = ["ID", "Name", "Flight #", "From", "To", "Date", "Seat", "Actions"]
        header_frame = tk.Frame(self)
        header_frame.pack()
        for h in headers:
            tk.Label(header_frame, text=h, font=("Arial", 10, "bold"), width=12, borderwidth=1, relief="solid").pack(side="left")

        self.data_frame = tk.Frame(self)
        self.data_frame.pack(pady=10)

        tk.Button(self, text="Back to Home", font=("Arial", 12), bg="#f44336", fg="white", width=20,
                  command=lambda: controller.show_frame("HomePage")).pack(pady=10)

        self.load_reservations()

    def load_reservations(self):
        for widget in self.data_frame.winfo_children():
            widget.destroy()

        reservations = database.get_all_reservations()
        for row in reservations:
            row_frame = tk.Frame(self.data_frame)
            row_frame.pack(pady=2)
            for item in row:
                tk.Label(row_frame, text=item, width=12, borderwidth=1, relief="solid").pack(side="left")
            tk.Button(row_frame, text="Edit", width=6, bg="#FFC107",
                      command=lambda r=row: self.edit_reservation(r)).pack(side="left", padx=2)
            tk.Button(row_frame, text="Delete", width=6, bg="#F44336", fg="white",
                      command=lambda r=row: self.delete_reservation(r)).pack(side="left", padx=2)

    def edit_reservation(self, row_data):
        self.controller.frames["EditReservationPage"].load_data({
            "id": row_data[0],
            "name": row_data[1],
            "flight_number": row_data[2],
            "departure": row_data[3],
            "destination": row_data[4],
            "date": row_data[5],
            "seat_number": row_data[6],
        })
        self.controller.show_frame("EditReservationPage")

    def delete_reservation(self, row_data):
        if messagebox.askyesno("Delete", f"Are you sure you want to delete reservation ID {row_data[0]}?"):
            database.delete_reservation(row_data[0])
            self.load_reservations()