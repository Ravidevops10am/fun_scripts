import pyautogui
import random
import time
import tkinter as tk

def toggle_wiggles():
    running.set(not running.get())
    wiggles()

def close_box():
    root.destroy()

def wiggles():
    if not running.get():
        return
    x = random.randint(-3,3)
    y = random.randint(-3,3)
    time_interval = random.randint(20,50) * 1000
    pyautogui.moveRel(x,y)
    root.after(time_interval, wiggles)

root = tk.Tk()

running = tk.BooleanVar()

tk.Button(root,text='Start/Stop',command=toggle_wiggles).grid(row=0,column=0)
tk.Button(root,text='Quit',command=close_box).grid(row=0,column=2)

root.mainloop()
