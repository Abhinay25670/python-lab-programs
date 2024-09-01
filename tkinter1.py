import tkinter as tk

top = tk.Tk()
top.title("Simple Tkinter GUI")
top.geometry("400x300")
label= tk.Label(top,text="hello")
label.pack(pady=20)

top.mainloop()