import tkinter as tk
from tkinter import messagebox
import time
from read_csv import ReadCSV

class App:
    def __init__(self):
        self.root = tk.Tk()

        self.select_room_button = tk.Button(self.root, text="Select a room", command=self.select_room)
        self.start_timer_button = tk.Button(self.root, text="Start the timer", command=self.start_timer)
        self.stop_timer_button = tk.Button(self.root, text="Stop the timer", command=self.stop_timer)
        self.select_room_entry = tk.Entry(self.root)
        self.id_entry = tk.Entry(self.root)
        self.read_csv = ReadCSV()
        self.data = {1: None, 2: None, 3: None, 4: None}
        self.id_list = self.read_csv.read_csv()
        self.time = time

        self.run()

    def select_room(self):
        room = self.select_room_entry.get()

        room = self.validate_room(room)

        if room:
            self.room = room
            if self.data[room]:
                self.stop_timer_button.pack()
                return
            self.id_entry.pack()
            self.start_timer_button.pack()

        return

    def validate_room(self, room):
        if not room:
            messagebox.showerror("Error", "The room entry was left blank")
            return None
        
        if not room.isdigit():
            messagebox.showerror("Error", "That is not a valid room")
            return None
        
        room = int(room)

        if not 1 <= room <= 4:
            messagebox.showerror("Error", "That is not a valid room")
            return None

        return room
    
    def start_timer(self):
       id = self.id_entry.get()
       id = self.validate_id(id)
       if not id:
           return
       
       self.data[self.room] = [id, self.time.time()]

       self.start_timer_button.pack_forget()
       self.id_entry.pack_forget()

       

    def validate_id(self, id):
        if not id:
            messagebox.showerror("Error", "The ID entry was left blank")
            return None

        if not id.isdigit():
            messagebox.showerror("Error", "The ID is not valid")
            return None

        for ids in self.id_list:
            if id == ids[0]:
                return id

        return None
    
    def stop_timer(self):
        stop_time = self.time.time()
        id, start_time = self.data[self.room]
        final_time = stop_time - start_time

        for ids in self.id_list:
            if id == ids[0]:
                username = ids[1]
        print(f"Time spent by {username} in room {self.room} was {final_time}")
        self.stop_timer_button.pack_forget()
        self.read_csv.save_csv({"name": username, "room": self.room, "times": final_time})
        
    def run(self):
        self.select_room_entry.pack()
        self.select_room_button.pack()
        self.root.geometry("640x480")
        self.root.mainloop()