import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StudentDatabaseGUI:
    def __init__(self, master):
        self.master = master
        master.title("Student Database")

        # Create frames for better organization
        self.student_frame = ttk.Labelframe(master, text="Student")
        self.student_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.section_frame = ttk.Labelframe(master, text="Section")
        self.section_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.instructor_frame = ttk.Labelframe(master, text="Instructor")
        self.instructor_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.course_frame = ttk.Labelframe(master, text="Course")
        self.course_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        # Student Frame
        self.student_id_label = ttk.Label(self.student_frame, text="Student ID:")
        self.student_id_label.grid(row=0, column=0, padx=5, pady=5)
        self.student_id_entry = ttk.Entry(self.student_frame)
        self.student_id_entry.grid(row=0, column=1, padx=5, pady=5)

        self.first_name_label = ttk.Label(self.student_frame, text="First Name:")
        self.first_name_label.grid(row=1, column=0, padx=5, pady=5)
        self.first_name_entry = ttk.Entry(self.student_frame)
        self.first_name_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons
        self.add_student_button = ttk.Button(master, text="Add Student", command=self.add_student)
        self.add_student_button.grid(row=2, column=0, padx=10, pady=10)

    def add_student(self):
        # Get data from the GUI
        student_id = self.student_id_entry.get()
        first_name = self.first_name_entry.get()

        # Validate and insert data into the database 
        # Clear the input fields
        self.student_id_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        # ... (clear other fields)

        messagebox.showinfo("Success", "Student added successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDatabaseGUI(root)
    root.mainloop()