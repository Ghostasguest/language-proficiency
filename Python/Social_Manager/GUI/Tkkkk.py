import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
import os
from datetime import datetime
import subprocess

# Function to handle the file upload
def upload_video(row_index):
    file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.avi;*.mov")])
    if file_path:
        destination = os.path.join('app_directory', os.path.basename(file_path))
        os.makedirs('app_directory', exist_ok=True)
        with open(file_path, 'rb') as fsrc:
            with open(destination, 'wb') as fdst:
                fdst.write(fsrc.read())
        video_paths[row_index].set(destination)

# Function to trigger another Python application
def trigger_upload_app():
    subprocess.Popen(["python", "another_application.py"])

# Function to delete a row
def delete_row(row_index):
    for widget in frame.grid_slaves():
        if int(widget.grid_info()["row"]) == row_index:
            widget.grid_forget()
    serial_numbers.pop(row_index - 1)
    title_entries.pop(row_index - 1)
    category_entries.pop(row_index - 1)
    video_upload_buttons.pop(row_index - 1)
    video_paths.pop(row_index - 1)
    privacy_statuses.pop(row_index - 1)
    description_entries.pop(row_index - 1)
    keyword_entries.pop(row_index - 1)
    date_entries.pop(row_index - 1)
    hour_selectors.pop(row_index - 1)
    minute_selectors.pop(row_index - 1)
    update_serial_numbers()
    global row_count
    row_count -= 1
    delete_from_db(row_index-1)
    add_row(is_label_row=True)
    load_data()

#Update serial_numbers
def update_serial_numbers():
    for index, label in enumerate(serial_numbers):
        label.config(text=str(index+1))

# Function to delete the corresponding row from the database
def delete_from_db(row_index):
    print(row_index)
    print(serial_numbers)
    serial_number = serial_numbers[row_index].cget("text")
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='client_upload'
        )
        cursor = conn.cursor()
        cursor.execute('DELETE FROM videos WHERE serial_number = %s', (serial_number,))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Success", f"Row {row_index} deleted successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to save the form data to a MySQL database
def save_data():
    for i in range(0, row_count-1):
        date_time = f"{date_entries[i].get()} {hour_selectors[i].get()}:{minute_selectors[i].get()}:00"
        data = {
            'Serial Number': serial_numbers[i].cget("text"),
            'Title': title_entries[i].get(),
            'Category': category_entries[i].get(),
            'Video Path': video_paths[i].get(),
            'Privacy Status': privacy_statuses[i].get(),
            'Description': description_entries[i].get(),
            'Keywords': keyword_entries[i].get(),
            'Date and Time': date_time
        }
        
        # Establish a connection to the MySQL database
        try:
            conn = mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='root',
                database='client_upload'
            )
            cursor = conn.cursor()

            # Create table if it doesn't exist
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS videos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    serial_number VARCHAR(255),
                    title VARCHAR(255),
                    category VARCHAR(255),
                    video_path VARCHAR(255),
                    privacy_status VARCHAR(255),
                    description TEXT,
                    keywords VARCHAR(255),
                    date_time DATETIME
                )
            ''')

            # Check if the serial number already exists
            cursor.execute('SELECT COUNT(*) FROM videos WHERE serial_number = %s', (data['Serial Number'],))
            result = cursor.fetchone()
            if result[0] == 0:
                # Insert data into the table
                cursor.execute('''
                    INSERT INTO videos (serial_number, title, category, video_path, privacy_status, description, keywords, date_time)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ''', (
                    data['Serial Number'],
                    data['Title'],
                    data['Category'],
                    data['Video Path'],
                    data['Privacy Status'],
                    data['Description'],
                    data['Keywords'],
                    data['Date and Time']
                ))

                # Commit the transaction
                conn.commit()

            # Close the connection
            cursor.close()
            conn.close()

            messagebox.showinfo("Success", "Data saved successfully!")

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")

# Function to load existing data from the MySQL database
def load_data():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            database='client_upload'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT serial_number, title, category, video_path, privacy_status, description, keywords, date_time FROM videos')
        rows = cursor.fetchall()
        for row in rows:
            serial_number, title, category, video_path_data, privacy_status_data, description, keywords, date_time = row
            date_time_str = date_time.strftime('%Y-%m-%d %H:%M:%S')
            date, time = date_time_str.split()
            add_row(data=(serial_number, title, category, video_path_data, privacy_status_data, description, keywords, date, time))
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

# Function to add a new row of widgets
def add_row(is_label_row=False, data=None):
    global row_count

    if is_label_row:
        # Create the header row with labels
        labels = ["Select", "Serial Number", "Title", "Category", "Video Upload", "Video Path", "Privacy Status", "Description", "Keywords", "Date", "Time", "Actions"]
        for col, label in enumerate(labels):
            label_widget = tk.Label(frame, text=label, anchor='center')
            label_widget.grid(row=row_count, column=col, padx=5, pady=10, sticky="nsew")
    else:
        if data:
            title, category, video_path_data, privacy_status_data, description, keywords, date, time = data
            hour, minute, _ = time.split(':')
        else:
            title = category = video_path_data = description = keywords = ""
            date = datetime.now().strftime('%Y-%m-%d')
            hour = datetime.now().strftime('%H')
            minute = datetime.now().strftime('%M')
            privacy_status_data = "Public"

        # Checkbox
        checkbox_var = tk.IntVar()
        checkbox = tk.Checkbutton(frame, variable=checkbox_var)
        checkbox.grid(row=row_count, column=0, padx=40, pady=40, sticky="nsew")

        # Serial Number
        serial_number_label = tk.Label(frame, text=str(row_count), anchor='center')
        serial_number_label.grid(row=row_count, column=1, padx=5, pady=10, sticky="nsew")
        serial_numbers.append(serial_number_label)

        # Title
        title_entry = tk.Entry(frame, justify='center')
        title_entry.insert(0, title)
        title_entry.grid(row=row_count, column=2, padx=5, pady=10, sticky="nsew")
        title_entries.append(title_entry)

        # Category
        category_entry = tk.Entry(frame, justify='center')
        category_entry.insert(0, category)
        category_entry.grid(row=row_count, column=3, padx=5, pady=10, sticky="nsew")
        category_entries.append(category_entry)

        # Video Upload
        video_path_var = tk.StringVar()
        video_path_var.set(video_path_data)
        video_paths.append(video_path_var)
        video_upload_button = tk.Button(frame, text="Upload Video", command=lambda row_index=row_count-1: upload_video(row_index))
        video_upload_button.grid(row=row_count, column=4, padx=5, pady=10, sticky="nsew")
        video_upload_buttons.append(video_upload_button)
        video_path_label = tk.Label(frame, textvariable=video_path_var, anchor='center')
        video_path_label.grid(row=row_count, column=5, padx=5, pady=10, sticky="nsew")

        # Privacy Status
        privacy_status = tk.StringVar()
        privacy_status.set(privacy_status_data)
        privacy_options = ttk.Combobox(frame, textvariable=privacy_status, values=["Public", "Private"], justify='center')
        privacy_options.grid(row=row_count, column=6, padx=5, pady=10, sticky="nsew")
        privacy_statuses.append(privacy_status)

        # Description
        description_entry = tk.Entry(frame, justify='center')
        description_entry.insert(0, description)
        description_entry.grid(row=row_count, column=7, padx=5, pady=10, sticky="nsew")
        description_entries.append(description_entry)

        # Keywords
        keywords_entry = tk.Entry(frame, justify='center')
        keywords_entry.insert(0, keywords)
        keywords_entry.grid(row=row_count, column=8, padx=5, pady=10, sticky="nsew")
        keyword_entries.append(keywords_entry)

        # Date
        date_picker = DateEntry(frame, date_pattern='yyyy-mm-dd')
        date_picker.set_date(date)
        date_picker.grid(row=row_count, column=9, padx=5, pady=10, sticky="nsew")
        date_entries.append(date_picker)

        # Time
        time_frame = tk.Frame(frame)
        time_frame.grid(row=row_count, column=10, padx=5, pady=10, sticky="nsew")
        hour_selector = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(24)], width=2, justify='center')
        hour_selector.set(hour)
        hour_selector.pack(side=tk.LEFT, padx=(0, 2))
        hour_selectors.append(hour_selector)
        minute_selector = ttk.Combobox(time_frame, values=[f"{i:02d}" for i in range(60)], width=2, justify='center')
        minute_selector.set(minute)
        minute_selector.pack(side=tk.LEFT)
        minute_selectors.append(minute_selector)

        # Actions
        action_frame = tk.Frame(frame)
        action_frame.grid(row=row_count, column=11, padx=5, pady=10, sticky="nsew")
        delete_button = tk.Button(action_frame, text="Delete", command=lambda row_index=row_count: delete_row(row_index))
        delete_button.pack(side=tk.LEFT, padx=(0, 5))
        upload_button = tk.Button(action_frame, text="Upload", command=trigger_upload_app)
        upload_button.pack(side=tk.LEFT)

    row_count += 1
    update_serial_numbers()


# Create the main application window
root = tk.Tk()
root.title("Grid Layout Example")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()-100

# Set the window size and position to be maximized
root.geometry(f"{screen_width}x{screen_height}+0+0")

# Create a frame for the scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas and a scrollbar
canvas = tk.Canvas(main_frame)
scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas
frame = tk.Frame(canvas)
canvas.create_window((0,0), window=frame, anchor='nw')

# Configure columns to expand proportionally
for col in range(12):
    frame.columnconfigure(col, weight=1)

# Initialize row count
row_count = 0

# Create a button to add new rows
add_row_button = tk.Button(root, text="Add Row", command=lambda: add_row(is_label_row=False))
add_row_button.pack(pady=10)

# Variables for video path
serial_numbers = []
title_entries = []
category_entries = []
video_upload_buttons = []
video_paths = []
privacy_statuses = []
description_entries = []
keyword_entries = []
date_entries = []
hour_selectors = []
minute_selectors = []

# Create the header row with labels
add_row(is_label_row=True)

# Load existing data from the database
load_data()

# Update the scroll region
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", on_frame_configure)

# Create a button to save data
save_button = tk.Button(root, text="Save", command=save_data)
save_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
