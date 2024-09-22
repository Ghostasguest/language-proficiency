import tkinter as tk
from textwrap import TextWrapper
from tkinter import ttk
from tkinter import font
from wsgiref import validate
import password_generator


# create a main frame
root = tk.Tk()
root.title("Password Generator")

custom_font = font.Font(size = 13)

def copy_to_clipboard():
    text = text_wrapper.get('1.0', 'end-1c')
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def validate_integer_input(input_value):
    # Allow empty input (optional)
    if input_value == "":
        return True

    # Check if the input is a valid integer
    if input_value.isdigit():
        return True
    else:
        return False

def update_output(generated_password):
    text_wrapper.delete("1.0", tk.END)
    text_wrapper.insert(tk.END, generated_password)

def initiate_password_generation():
    generated_pass = ""
    password_generator.length = int(length.get())
    password_generator.upper = int(capitals.get())
    password_generator.lower = int(lower.get())
    password_generator.number = int(numerical.get())
    password_generator.special = int(special.get())

    password_generator.args = {
        'caps': password_generator.upper ,
        'small': password_generator.lower,
        'special_chars': password_generator.special,
        'nums': password_generator.number
    }

    generated_pass = "".join(password_generator.generate_password(password_generator.length))
    password_generator.reset_counter()
    print(generated_pass)
    update_output(generated_pass)


# Adding columns in the GUI
tk.Label(root, text="Length of the password: ", font = custom_font).grid(row = 0, column = 0,padx=20, pady=20, sticky = "w")

validate_command = root.register(validate_integer_input)
length = tk.Entry(root, validate = 'key', validatecommand=(validate_command, '%P'))
length.grid(row=0, column=1, padx=20, pady=20, sticky = "w")

# Capitals Checkbox
label = tk.Label(root, text = "Include uppercase.", font = custom_font)
label.grid(row=1, column=0, padx=20, pady=20, sticky='w')

capitals = tk.BooleanVar()
cb1 = tk.Checkbutton(root, variable = capitals, font = custom_font)
cb1.grid(row = 1, column = 1, padx=20, pady=0, sticky = "w")


# Lowercase checkbox
label = tk.Label(root, text = "Include lowercase", font = custom_font)
label.grid(row=2, column=0, padx=20, pady=20, sticky='w')

lower = tk.BooleanVar()
cb2 = tk.Checkbutton(root, variable = lower, font = custom_font)
cb2.grid(row = 2, column = 1, padx=20, pady=0, sticky = "w")


# Numerical values
label = tk.Label(root, text = "Include numericals.", font = custom_font)
label.grid(row=3, column=0, padx=20, pady=20, sticky='w')

numerical = tk.BooleanVar()
cb3 = tk.Checkbutton(root, variable = numerical, font = custom_font)
cb3.grid(row = 3, column = 1, padx=20, pady=0, sticky = "w")


# Special characters checkbox
label = tk.Label(root, text = "Include special characters.", font = custom_font)
label.grid(row=4, column=0, padx=20, pady=20, sticky='w')

special = tk.BooleanVar()
cb4 = tk.Checkbutton(root, variable = special, font = custom_font)
cb4.grid(row = 4, column = 1, padx=20, pady=0, sticky = "w")

#text box to display the password
text_wrapper = tk.Text(root, wrap = "word", font = custom_font, height = 1.5, width = 50)
text_wrapper.grid(row = 5, padx=20, pady=0, sticky = "w")



# creating a frame and holding buttons
frame = tk.Frame(root)
frame.grid(row=5, column=1, padx=10, pady=10)

# Copy button
button = tk.Button(frame, text = "copy", font = custom_font, command = copy_to_clipboard)
button.grid(row = 0, column = 0, padx=20, pady=0, sticky = "w")

#generate button
button = tk.Button(frame, text = "Generate", font = custom_font, command=initiate_password_generation)
button.grid(row = 0, column = 1, padx=20, pady=20, sticky = "e")

root.mainloop()
