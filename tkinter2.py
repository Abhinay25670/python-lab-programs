import tkinter as tk

top = tk.Tk()
top.title("button")
top.geometry("400x300")
label = tk.Label(top,text="hello")
label.pack(pady=20)
button = tk.Button(top,text="submit",command=lambda:label.config(text="Good Bye"))
button.pack()
button = tk.Button(top,text="submit",command=lambda:label.config(text="hello"))
button.pack()
top.mainloop()