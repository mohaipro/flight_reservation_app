import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="\u2708\ufe0f Flight Reservation System", font=("Arial", 24, "bold"))
        label.pack(pady=50)

        tk.Button(self, text="Book Flight", font=("Arial", 14), width=20, height=2, bg="#4CAF50", fg="white",
                  command=lambda: controller.show_frame("BookingPage")).pack(pady=20)

        tk.Button(self, text="View Reservations", font=("Arial", 14), width=20, height=2, bg="#2196F3", fg="white",
                  command=lambda: controller.show_frame("ReservationsPage")).pack(pady=10)