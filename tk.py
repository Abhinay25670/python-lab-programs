from tkinter import *

t = Tk()
t.geometry('460x450')

# Create a Frame with a border to contain the form widgets
form_frame = Frame(t, bd=2, relief="solid", padx=10, pady=10)
form_frame.pack(pady=20, padx=20)  # Use pack to place the frame with padding

# Add the form widgets inside the bordered frame
Label(form_frame, text="Enter Name\t\t").grid(row=0, column=0, sticky="w")
Label(form_frame, text=" ").grid(row=1, column=0)
Label(form_frame, text="Enter Email\t\t").grid(row=2, column=0, sticky="w")
Label(form_frame, text=" ").grid(row=3, column=0)
Label(form_frame, text="Contact Number\t\t").grid(row=4, column=0, sticky="w")
Label(form_frame, text=" ").grid(row=5, column=0)
Label(form_frame, text="Select Gender\t\t").grid(row=6, column=0, sticky="w")
Label(form_frame, text=" ").grid(row=7, column=0)
Label(form_frame, text="Select Country\t\t").grid(row=8, column=0, sticky="w")
Label(form_frame, text=" ").grid(row=9, column=0)
Label(form_frame, text="Enter Password\t\t").grid(row=10, column=0, sticky="w")
Label(form_frame, text=" ").grid(row=11, column=0)
Label(form_frame, text="Re-Enter Password\t").grid(row=12, column=0, sticky="w")
Label(form_frame, text=" ").grid(row=13, column=0)

#select Gender
selected_gender = StringVar(value="Male")
# Entry widgets
Entry(form_frame, bd=5).grid(row=0, column=1, padx=5)
Entry(form_frame, bd=5).grid(row=2, column=1, padx=5)
Entry(form_frame, bd=5).grid(row=4, column=1, padx=5)
Entry(form_frame, bd=5).grid(row=8, column=1, padx=5)
Entry(form_frame, bd=5).grid(row=10, column=1, padx=5)
Entry(form_frame, bd=5).grid(row=12, column=1, padx=5)

# Radio buttons in the same row with even spacing
radio_frame = Frame(form_frame)
radio_frame.grid(row=6, column=1, columnspan=3, sticky="w")
Radiobutton(radio_frame, text="Male",variable=selected_gender,value="Male").pack(side=LEFT, padx=10)
Radiobutton(radio_frame, text="Female",variable=selected_gender,value="Female").pack(side=LEFT, padx=10)
Radiobutton(radio_frame, text="Others",variable=selected_gender,value="others").pack(side=LEFT, padx=10)



# Button widget
Button(form_frame, text="Register", bd=3).grid(row=14, column=0, columnspan=2, pady=10)

t.mainloop()