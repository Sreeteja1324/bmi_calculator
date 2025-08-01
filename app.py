import tkinter as tk
from tkinter import messagebox, scrolledtext

def get_suggestion(bmi):
    if bmi < 16:
        return (
            "You are severely underweight.\n\n"
            "🥗 Suggestions:\n"
            "- Eat calorie-dense foods like nuts, dairy, and lean proteins\n"
            "- Eat more frequently (5-6 small meals a day)\n"
            "- Consult a nutritionist for a supervised plan"
        )
    elif 16 <= bmi < 18.5:
        return (
            "You are underweight.\n\n"
            "🥗 Suggestions:\n"
            "- Increase healthy fats and protein intake\n"
            "- Add smoothies or shakes to your meals\n"
            "- Strength training to build muscle mass"
        )
    elif 18.5 <= bmi < 20.5:
        return (
            "You are in the lower range of normal weight.\n\n"
            "🙂 Suggestions:\n"
            "- Maintain your current weight with a balanced diet\n"
            "- Focus on lean proteins and moderate exercise\n"
            "- Monitor for unintentional weight loss"
        )
    elif 20.5 <= bmi < 23:
        return (
            "You are comfortably within the normal weight range.\n\n"
            "✅ Suggestions:\n"
            "- Keep up your regular eating and activity patterns\n"
            "- Maintain hydration and sleep hygiene\n"
            "- Routine physical checkups recommended"
        )
    elif 23 <= bmi < 24.9:
        return (
            "You are in the higher range of normal weight.\n\n"
            "🧘 Suggestions:\n"
            "- Watch portion sizes and limit processed foods\n"
            "- Maintain active lifestyle and monitor weight trends\n"
            "- Focus on stress management"
        )
    elif 25 <= bmi < 27.5:
        return (
            "You are moderately overweight.\n\n"
            "🏃 Suggestions:\n"
            "- Start moderate cardio and reduce sugary drinks\n"
            "- Log meals to become aware of eating patterns\n"
            "- Add more fiber to your diet"
        )
    elif 27.5 <= bmi < 29.9:
        return (
            "You are overweight.\n\n"
            "💪 Suggestions:\n"
            "- Focus on strength and aerobic training\n"
            "- Consider intermittent fasting (if medically safe)\n"
            "- Cook at home more often to control calories"
        )
    elif 30 <= bmi < 35:
        return (
            "You are in Obesity Class I.\n\n"
            "⚠️ Suggestions:\n"
            "- Seek a customized plan from a healthcare provider\n"
            "- Increase daily movement (walks, stretching)\n"
            "- Monitor blood pressure, glucose, and cholesterol"
        )
    elif 35 <= bmi < 40:
        return (
            "You are in Obesity Class II.\n\n"
            "🚨 Suggestions:\n"
            "- Join a structured weight loss program\n"
            "- Limit screen time and prioritize sleep\n"
            "- Address emotional eating or stress factors"
        )
    else:
        return (
            "You are in Obesity Class III (Severe).\n\n"
            "🛑 Suggestions:\n"
            "- Urgently consult a doctor for medical management\n"
            "- Consider clinical support (dietician, therapist)\n"
            "- Focus on sustainable lifestyle changes"
        )

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Input Error", "Weight and height must be positive numbers.")
            return

        bmi = weight / (height ** 2)

        # Determine display style
        if bmi < 18.5:
            category = "Underweight"
            color = "#87CEEB"
            emoji = "🥗"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
            color = "#90EE90"
            emoji = "🙂"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            color = "#FFD700"
            emoji = "🏃"
        else:
            category = "Obese"
            color = "#FF6347"
            emoji = "⚠️"

        result_label.config(
            text=f"{emoji} Your BMI is: {bmi:.2f}\nCategory: {category}",
            bg=color
        )
        output_frame.config(bg=color)
        suggestion_text.config(state='normal')
        suggestion_text.delete("1.0", tk.END)
        suggestion_text.insert(tk.END, get_suggestion(bmi))
        suggestion_text.config(state='disabled', bg=color)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("960x540")
root.configure(bg="#f0f8ff")
root.resizable(False, False)

# Title
tk.Label(root, text="BMI Calculator", font=("Helvetica", 28, "bold"),
         bg="#f0f8ff", fg="#222").pack(pady=15)

# Input Frame
input_frame = tk.Frame(root, bg="#f0f8ff")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Weight (kg):", font=("Helvetica", 16), bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5, sticky='e')
weight_entry = tk.Entry(input_frame, font=("Helvetica", 16), width=10, justify='center')
weight_entry.grid(row=0, column=1, padx=10)

tk.Label(input_frame, text="Height (m):", font=("Helvetica", 16), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5, sticky='e')
height_entry = tk.Entry(input_frame, font=("Helvetica", 16), width=10, justify='center')
height_entry.grid(row=1, column=1, padx=10)

# Calculate button
tk.Button(root, text="Calculate BMI", command=calculate_bmi,
          font=("Helvetica", 16, "bold"), bg="#4CAF50", fg="white",
          padx=15, pady=8).pack(pady=20)

# Output Frame
output_frame = tk.Frame(root, bg="#f0f8ff", bd=3, relief="groove")
output_frame.pack(pady=10, padx=30, fill="both", expand=True)

# Result Label
result_label = tk.Label(output_frame, text="", font=("Helvetica", 22, "bold"),
                        bg="#f0f8ff", fg="#222", justify="center")
result_label.pack(pady=(10, 5))

# Suggestion Box
suggestion_text = scrolledtext.ScrolledText(output_frame, font=("Helvetica", 16),
                                             wrap=tk.WORD, height=10, width=80,
                                             bg="#f0f8ff", fg="#333", borderwidth=2, relief="ridge")
suggestion_text.pack(pady=10, padx=15)
suggestion_text.config(state='disabled')

# Run the GUI
root.mainloop()
