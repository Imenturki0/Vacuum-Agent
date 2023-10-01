import tkinter as tk

class VacuumCleanerAgent:
    def __init__(self, master):
        self.master = master
        master.title("Vacuum Cleaner Agent")

        self.canvas = tk.Canvas(master, width=400, height=300, bg="lightgray")
        self.canvas.pack()

        # Draw rectangles for locations A and B
        self.rect_a = self.canvas.create_rectangle(50, 50, 150, 150, outline="black", fill="lightgreen", width=2)
        self.canvas.tag_bind(self.rect_a, "<Button-1>", lambda event, location="A": self.toggle_cleanliness(location))
        self.canvas.create_text(100, 100, text="A", font=("Arial", 20, "bold"))

        self.rect_b = self.canvas.create_rectangle(250, 50, 350, 150, outline="black", fill="lightgreen", width=2)
        self.canvas.tag_bind(self.rect_b, "<Button-1>", lambda event, location="B": self.toggle_cleanliness(location))
        self.canvas.create_text(300, 100, text="B", font=("Arial", 20, "bold"))

        self.status_label = tk.Label(master, text="Vacuum cleaner is at location A", font=("Arial", 14))
        self.status_label.pack(pady=10)

        self.locations = {
            "A": {"status": "Clean"},
            "B": {"status": "Clean"}
        }
        self.location = "A"

        self.scheduled_operations = []
        self.auto_operations()

        self.master.bind("<Key>", self.stop_operations)

    def auto_operations(self):
        self.move()
        self.scheduled_operations.append(self.master.after(2000, self.clean))  # Clean after a delay of 2 seconds
        self.scheduled_operations.append(self.master.after(4000, self.auto_operations))  # Repeat after 4 seconds
        #self.master.after(2000, self.clean)  # Clean after a delay of 2 seconds
       # self.master.after(4000, self.auto_operations)  # Repeat after 4 seconds

    def move(self):
        if self.location == "A":
            destination = "B"
        else:
            destination = "A"

        self.status_label.config(text=f"Moving to location {destination}")
        print(f"Moving to location {destination}")
        self.location = destination

    def clean(self):
        if self.locations[self.location]["status"] == "Dirty":
            self.status_label.config(text=f"Vacuum cleaner cleaned {self.location}")
            print(f"Vacuum cleaner cleaned {self.location}")
            self.locations[self.location]["status"] = "Clean"
            if self.location == "A":
                self.canvas.itemconfig(self.rect_a, fill="lightgreen")
            else:
                self.canvas.itemconfig(self.rect_b, fill="lightgreen")

    def toggle_cleanliness(self, location):
        if self.locations[location]["status"] == "Clean":
            self.locations[location]["status"] = "Dirty"
            if location == "A":
                self.canvas.itemconfig(self.rect_a, fill="red")
            else:
                self.canvas.itemconfig(self.rect_b, fill="red")
        else:
            self.locations[location]["status"] = "Clean"
            if location == "A":
                self.canvas.itemconfig(self.rect_a, fill="lightgreen")
            else:
                self.canvas.itemconfig(self.rect_b, fill="lightgreen")
    def stop_operations(self, event):
        if event.keysym == 'space':
            for operation in self.scheduled_operations:
                self.master.after_cancel(operation)
            self.status_label.config(text="Automatic operation stopped.")

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("450x400")
    root.configure(bg="lightgray")
    vacuum_agent = VacuumCleanerAgent(root)
    root.mainloop()
