import tkinter as tk
from tkinter import messagebox

class CGPACalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("CGPA Calculator")
        self.entries = []
        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.root, text="Enter number of subjects:").grid(row=0, column=0, pady=10)
        self.num_subjects_entry = tk.Entry(self.root)
        self.num_subjects_entry.grid(row=0, column=1)
        
        self.generate_btn = tk.Button(self.root, text="Generate Fields", command=self.generate_fields)
        self.generate_btn.grid(row=0, column=2, padx=10)
        
        self.calculate_btn = tk.Button(self.root, text="Calculate CGPA", command=self.calculate_cgpa)
        self.calculate_btn.grid(row=2, column=1, pady=10)
        self.calculate_btn.config(state='disabled')
        
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.grid(row=3, column=0, columnspan=3, pady=10)
        
    def generate_fields(self):
        try:
            n = int(self.num_subjects_entry.get())
            if n <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid positive integer for number of subjects.")
            return
        
        # Clear previous fields if any
        for widgets in self.entries:
            for w in widgets:
                w.destroy()
        self.entries.clear()
        
        # Create headers
        tk.Label(self.root, text="Subject").grid(row=4, column=0)
        tk.Label(self.root, text="Grade Point").grid(row=4, column=1)
        tk.Label(self.root, text="Credit Hours").grid(row=4, column=2)
        
        # Create entry fields
        for i in range(n):
            subj_label = tk.Label(self.root, text=f"Subject {i+1}")
            subj_label.grid(row=5+i, column=0, pady=2)
            grade_entry = tk.Entry(self.root, width=10)
            grade_entry.grid(row=5+i, column=1, pady=2)
            credit_entry = tk.Entry(self.root, width=10)
            credit_entry.grid(row=5+i, column=2, pady=2)
            self.entries.append((grade_entry, credit_entry))
        
        self.calculate_btn.config(state='normal')
        self.result_label.config(text="")
    
    def calculate_cgpa(self):
        total_points = 0
        total_credits = 0
        
        try:
            for grade_entry, credit_entry in self.entries:
                grade = float(grade_entry.get())
                credit = float(credit_entry.get())
                if grade < 0 or credit <= 0:
                    raise ValueError
                total_points += grade * credit
                total_credits += credit
            if total_credits == 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid positive numbers for grade points and credits.")
            return
        
        cgpa = total_points / total_credits
        self.result_label.config(text=f"Your CGPA is: {cgpa:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CGPACalculator(root)
    root.mainloop()
