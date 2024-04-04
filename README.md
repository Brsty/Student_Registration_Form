# Student_Registration_Form
Python Project using Tkinter
This Python script creates a simple student registration form GUI using the Tkinter library and generates a PDF document based on the entered data using the ReportLab library.

Here's a brief explanation of the project structure:

GUI Layout: The GUI consists of labels and entry fields for the user to input various details such as name, age, qualification, experience, email, phone number, and college name. The layout is structured using Tkinter's grid manager to organize widgets in rows and columns.

Data Validation: The script includes a validate_data() method to ensure that all required fields are filled, and the entered data meets certain criteria (e.g., age is numeric, email follows a valid format). It displays error messages using Tkinter's messagebox module if validation fails.

PDF Generation: Upon successful validation, the generate_pdf() method creates a PDF document using ReportLab. It retrieves the entered data from the GUI and draws it onto the PDF canvas in a structured format. The generated PDF is saved with the filename "student_registration.pdf".

Submit Form: The submit_form() method is called when the user clicks the submit button. It first validates the entered data and then generates the PDF if validation passes.

Main Function: The main() function initializes the Tkinter root window and creates an instance of the StudentRegistrationForm class, which sets up the GUI and handles user interactions.
