import tkinter as tk
import database
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

database.create_table()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation System")
        self.geometry("800x600")
        self.resizable(False, False)

        self.frames = {}
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.place(relwidth=1, relheight=1)

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

if __name__ == "__main__":
    app = App()
    app.mainloop()