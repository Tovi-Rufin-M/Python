from assets.data import ClockData
import tkinter as tk

class ClockApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clock App")

        self.time_label = tk.Label(self.root, font=("Silkscreen", 48), fg="black")
        self.time_label.pack(pady=20)

        self.date_label = tk.Label(self.root, font=("Silkscreen", 24), fg="black")
        self.date_label.pack(pady=10)

        self.update_clock()

    def update_clock(self):
        clock_data = ClockData()
        current_time = clock_data.time["time"]
        current_date = clock_data.date["date"]

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        # Schedule the update_clock function to run again after 1000 milliseconds (1 second)
        self.root.after(1000, self.update_clock)
    def show(self):
        self.root.mainloop()
