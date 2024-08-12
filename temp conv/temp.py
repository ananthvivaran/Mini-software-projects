import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = (celsius * 9/5) + 32
        label_result.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place the widgets
label_celsius = tk.Label(root, text="Celsius:")
label_celsius.grid(row=0, column=0, padx=10, pady=10)

entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1, padx=10, pady=10)

button_convert = tk.Button(root, text="Convert", command=convert_temperature)
button_convert.grid(row=1, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=2, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
