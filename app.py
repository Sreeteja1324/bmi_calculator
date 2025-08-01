import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f} ({category})")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Labels and Entry Boxes
tk.Label(root, text="Enter your weight (kg):").pack(pady=(10, 0))
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Enter your height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Calculate Button
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result Display
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Start GUI loop
root.mainloop()

