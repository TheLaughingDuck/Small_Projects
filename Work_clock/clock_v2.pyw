#%%
import tkinter as tk
from tkinter import messagebox
import math
import time
from datetime import datetime
import threading
import requests
import os
import dotenv

dotenv.load_dotenv()

# Grab database url and authentication token
DATABASE_URL=os.getenv("DATABASE_URL")
AUTH_TOKEN=os.getenv("AUTH_TOKEN")
HEADERS = {
    'Authorization': f'Bearer {AUTH_TOKEN}',
    'Content-Type': 'application/json'
}

def query(sql: str, args=None):
    '''
    Function used to send a PUT request to the database with todays information,
    like start and end times, and total working time.
    '''
    payload = {
        'requests': [
            {
                'type': 'execute',
                'stmt': {
                    'sql': sql,
                    'args': args or []
                }
            },
            {'type': 'close'}
        ]
    }

    response = requests.post(f'{DATABASE_URL}/v2/pipeline', json=payload, headers=HEADERS)
    return response.status_code

#query("INSERT INTO workdays (start_time) VALUES ('123')")
#%%

import sqlite3
def save_workday_data(start_time, end_time, hours):
    '''
    Creates a new record in the datebase file.
    '''
    conn = sqlite3.connect("data.sqlite3", isolation_level=None)
    conn.execute("CREATE TABLE IF NOT EXISTS 'workdays' (date STR DEFAULT NULL, start_time STR NOT NULL, end_time STR NOT NULL, hours REAL NOT NULL)")

    conn.execute(f"INSERT INTO 'workdays' (date, start_time, end_time, hours) VALUES ('{datetime.date(datetime.today())}', '{start_time}', '{end_time}', {hours})")

def save_workblock_data(start_time, end_time, hours):
    '''
    Creates a new record in the datebase file.
    '''
    conn = sqlite3.connect("data.sqlite3", isolation_level=None)
    conn.execute("CREATE TABLE IF NOT EXISTS 'workblocks' (date STR DEFAULT NULL, start_time STR NOT NULL, end_time STR NOT NULL, hours REAL NOT NULL)")

    conn.execute(f"INSERT INTO 'workblocks' (date, start_time, end_time, hours) VALUES ('{datetime.date(datetime.today())}', '{start_time}', '{end_time}', {hours})")

class TimerApp:
    GUI_WIDTH = 200
    GUI_HEIGHT = 60
    INTERVAL = 3600 #int(i) # Number of seconds

    def __init__(self, root):
        
        # Set up for tracking the start and end times of the working day, e.g. 08:03 and 17:06
        self.start_time_HH_MM = time.strftime('%H:%M')

        self.root = root
        self.root.title("Analog Timer")
        self.root.geometry(f"{self.GUI_WIDTH}x{self.GUI_HEIGHT+30}")  # Add space for session counter
        self.root.attributes('-topmost', True)
        self.root.resizable(True, True)#(False, False)

        self.canvas = tk.Canvas(root, width=self.GUI_WIDTH, height=self.GUI_HEIGHT, bg="white", highlightthickness=0)
        self.canvas.pack()

        self.session_label = tk.Label(root, text="Sessions Completed: 0", font=("Helvetica", 12))
        self.session_label.pack()

        self.running = True
        self.start_time = time.time()
        self.elapsed_time = 0
        self.session_count = 0

        self.padding = 10
        self.bar_width = 45
        self.bar_height = self.GUI_WIDTH - 2 * self.padding

        # Workblock timekeeping
        self.workblock_start = time.time()
        self.workblock_start_str = time.strftime('%H:%M')

        self.draw_progress_bar()
        self.update_bar()

        self.root.bind("<Button-1>", self.toggle_timer)  # Left-click to pause/resume
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def draw_progress_bar(self):
        self.canvas.create_rectangle(self.padding, self.padding, self.padding + self.bar_height, self.padding + self.bar_width, outline="black", width=2)

    def update_bar(self):
        self.canvas.delete("hands")
        self.canvas.delete("progress")

        # Draw progress indicator
        elapsed = (time.time() - self.start_time) + self.elapsed_time if self.running else self.elapsed_time
        self.remaining = max(self.INTERVAL - elapsed, 0)  # 1500 seconds = 25 minutes, 3600 seconds = 60 minutes
        proportion_left = 1-(elapsed / self.INTERVAL)

        if self.remaining > 0:
            # x_end = self.center + self.radius * math.cos(angle)
            # y_end = self.center + self.radius * math.sin(angle)
            # self.canvas.create_arc(10, 10, self.GUI_SIZE - 10, self.GUI_SIZE - 10, start=90, extent=-(elapsed / self.INTERVAL) * 360, fill="red", tags="progress")

            self.canvas.create_rectangle(self.padding, self.padding, self.padding + (1-proportion_left) * self.bar_height, self.padding + self.bar_width, fill="darkred", width=2, tags="progress")
            completion_percentage = round(100 * (self.session_count * 3600 + elapsed) / (5*3600))
            self.session_label.config(text=f"Workday completion: {completion_percentage} %")

        # # Draw hand (based on progress, not the current time)
        # x = self.center + self.radius * math.cos(angle)
        # y = self.center + self.radius * math.sin(angle)
        # self.canvas.create_line(self.center, self.center, x, y, fill="black", width=2, tags="hands")

        # Update timer display
        minutes = int((elapsed % 3600) // 60) #minutes = int(self.remaining // 60)
        seconds = int(elapsed % 60) #int((self.INTERVAL-self.remaining) % 60) #seconds = int(self.remaining % 60)
        #self.canvas.itemconfig("time", text=f"{minutes:02}:{seconds:02}")
        self.canvas.delete("time")
        label = f"{self.session_count}:{minutes:02}:{seconds:02}" if self.running else "Paused"
        #self.canvas.create_text(self.center, self.center, text=label, font=("Helvetica", int(self.GUI_SIZE * 0.08)), tags="time")
        self.canvas.create_text(self.GUI_WIDTH // 2, self.GUI_HEIGHT // 2 + 3, text=label, font=("Helvetica", int(self.GUI_WIDTH * 0.08)), tags="time")

        if self.remaining <= 0 and self.running:
            self.running = True
            self.elapsed_time = 0
            self.session_count += 1
            #self.session_label.config(text=f"Sessions Completed: {self.session_count}")
            
            #completion_percentage = round(100 * (self.session_count * 3600 + elapsed) / (5*3600), 1)
            #self.session_label.config(text=f"Workday completion: {completion_percentage} %")
            #messagebox.showinfo("Session Complete!", f"You completed session #{self.session_count}!")

            # Start over
            self.start_time = time.time()

        self.root.after(1000, self.update_bar)

    def toggle_timer(self, event=None):
        # PAUSE the clock!
        if self.running:
            self.running = False
            self.elapsed_time += time.time() - self.start_time

            # Update the workblock database
            hours = str(round((time.time() - self.workblock_start) / 3600, 2))
            save_workblock_data(self.workblock_start_str, time.strftime('%H:%M'), hours)

        # START the clock again!
        else:
            self.running = True
            self.start_time = time.time()

            # Start over timekeeping for the new workblock
            self.workblock_start = time.time()
            self.workblock_start_str = time.strftime('%H:%M')        

    def on_close(self):
        # If still running, also log the current workblock before submitting the workday and ending the program.
        # I do this by just toggling the clock on again, which triggers a save to the workblock table.
        if self.running:
            hours = str(round((time.time() - self.workblock_start) / 3600, 2))
            save_workblock_data(self.workblock_start_str, time.strftime('%H:%M'), hours)

        # Don't this is actually necessary here? It was at the top of on_close before.
        self.running = False

        # Save todays data in the database file
        self.end_time_HH_MM = time.strftime('%H:%M')
        hours = str(round(self.session_count + (1-self.remaining/self.INTERVAL), 1))
        save_workday_data(self.start_time_HH_MM, self.end_time_HH_MM, hours)
        
        # # Assemble sql PUT request that details what time the workday started and ended, and how many hours I studied.
        # self.end_time_HH_MM = time.strftime('%H:%M')
        # hours = str(round(self.session_count + (1-self.remaining/self.INTERVAL), 1))
        # sql = f"INSERT INTO workdays (start_time, hours, end_time) VALUES ('{self.start_time_HH_MM}', '{hours}', '{self.end_time_HH_MM}')"

        # try:
        #     query(sql)
        # except:
        #     raise ConnectionRefusedError("Something went wrong with the SQL request")

        # Destroy window
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()