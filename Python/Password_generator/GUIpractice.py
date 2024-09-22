import tkinter as tk
from dataclasses import field


def get_info():
    on_off = caps_checkbox_var.get()
    text = length_entry.get()
    print(text)
    print(on_off)

# create a main window
root = tk.Tk()
root.title("Password Generator")

# set initial size
root.geometry ("500x500")


# widgets

# label for entry field
length_label = tk.Label (root, text="Enter Length:")
length_label.pack()

# entry field
length_entry =tk.Entry(root)
length_entry.pack()

# button
button = tk.Button(root, text= "Generate", command = get_info)
button.pack()

# checkbox
caps_checkbox_var = tk.BooleanVar(value = True)
caps_checkbox = tk.Checkbutton(root, text = "true of false", variable = caps_checkbox_var)
caps_checkbox.pack()

# text widget
result_text =  tk.Text(root, wrap = "word", height = 1.5, width = 50, state = tk.DISABLED)
result_text.pack()

# run the application
root.mainloop()