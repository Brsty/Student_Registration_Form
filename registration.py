import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class StudentRegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Student Registration Form")

        # Full-page geometry
        master.geometry("500x400")
        master.configure(bg="#F0F0F0")  # Light gray background

        # Labels and entry fields
        self.label_name = tk.Label(master, text="Name:", bg="#F0F0F0", fg="black")  # Light gray background, black text
        self.label_name.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_name = tk.Entry(master, bg="white")  # White entry field
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_age = tk.Label(master, text="Age:", bg="#F0F0F0", fg="black")  # Light gray background, black text
        self.label_age.grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_age = tk.Entry(master, bg="white")  # White entry field
        self.entry_age.grid(row=1, column=1, padx=10, pady=10)

        self.label_qualification = tk.Label(master, text="Qualification:", bg="#F0F0F0", fg="black")  # Light gray background, black text
        self.label_qualification.grid(row=2, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_qualification = tk.Entry(master, bg="white")  # White entry field
        self.entry_qualification.grid(row=2, column=1, padx=10, pady=10)

        self.label_experience = tk.Label(master, text="Experience:", bg="#F0F0F0", fg="black")  # Light gray background, black text
        self.label_experience.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_experience = tk.Entry(master, bg="white")  # White entry field
        self.entry_experience.grid(row=3, column=1, padx=10, pady=10)

        self.label_email = tk.Label(master, text="Email:", bg="#F0F0F0", fg="black")  # Light gray background, black text
        self.label_email.grid(row=4, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_email = tk.Entry(master, bg="white")  # White entry field
        self.entry_email.grid(row=4, column=1, padx=10, pady=10)

        self.label_phone = tk.Label(master, text="Phone No:", bg="#F0F0F0", fg="black")  # Light gray background, black text
        self.label_phone.grid(row=5, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_phone = tk.Entry(master, bg="white")  # White entry field
        self.entry_phone.grid(row=5, column=1, padx=10, pady=10)

        self.label_college = tk.Label(master, text="College Name:", bg="#F0F0F0", fg="black")  # Light gray background, black text
        self.label_college.grid(row=6, column=0, sticky=tk.E, padx=10, pady=10)
        self.entry_college = tk.Entry(master, bg="white")  # White entry field
        self.entry_college.grid(row=6, column=1, padx=10, pady=10)

        # Submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form, bg="#007BFF", fg="white")  # Blue button
        self.submit_button.grid(row=7, columnspan=2, pady=10)

    def validate_data(self):
        name = self.entry_name.get()
        age = self.entry_age.get()
        qualification = self.entry_qualification.get()
        experience = self.entry_experience.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        college = self.entry_college.get()

        # Basic validation
        if not name or not age or not qualification or not experience or not email or not phone or not college:
            messagebox.showerror("Error", "Please fill in all fields")
            return False
        if not age.isdigit():
            messagebox.showerror("Error", "Age should be a numeric value")
            return False
        if not email.endswith('@gmail.com'):  
            messagebox.showerror("Error", "Invalid email format")
            return False
        if not phone.isdigit():
            messagebox.showerror("Error", "Phone number should contain only digits")
            return False
        return True

    def generate_pdf(self):
        filename = "student_registration.pdf"
        name = self.entry_name.get()
        age = self.entry_age.get()
        qualification = self.entry_qualification.get()
        experience = self.entry_experience.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        college = self.entry_college.get()

        # PDF generation
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawString(100, 750, "Student Registration Form")
        c.drawString(100, 730, f"Name: {name}")
        c.drawString(100, 710, f"Age: {age}")
        c.drawString(100, 690, f"Qualification: {qualification}")
        c.drawString(100, 670, f"Experience: {experience}")
        c.drawString(100, 650, f"Email: {email}")
        c.drawString(100, 630, f"Phone No: {phone}")
        c.drawString(100, 610, f"College Name: {college}")
        c.save()
        messagebox.showinfo("Success", f"PDF generated successfully: {filename}")

    def submit_form(self):
        if self.validate_data():
            self.generate_pdf()

def main():
    root = tk.Tk()
    app = StudentRegistrationForm(root)
    root.mainloop()

if __name__ == "__main__":
    main()


