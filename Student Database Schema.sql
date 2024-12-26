CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    major VARCHAR(50),
    gpa DECIMAL(3,2) CHECK (gpa >= 0.0 AND gpa <= 4.0),
    email VARCHAR(100), 
    phone_number VARCHAR(20) 
);
CREATE TABLE Section (
    section_id INT PRIMARY KEY,
    course_id INT REFERENCES Course(course_id),
    semester VARCHAR(20),
    Room INT,
    Time TIME,
    instructor_id INT REFERENCES Instructor(instructor_id),
    room VARCHAR(50) 
);
CREATE TABLE Instructor (
    instructor_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department VARCHAR(50)
);
CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT, 
    student_id INT REFERENCES Student(student_id),
    section_id INT REFERENCES Section(section_id),
    enrollment_date DATE,
    grade VARCHAR(2) 
);
CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT,
    department VARCHAR(50)
);
CREATE INDEX idx_student_name ON Student (first_name, last_name);
CREATE INDEX idx_course_name ON Course (course_name);
CREATE INDEX idx_section_course_year ON Section (course_id, year);
CREATE INDEX idx_enrollment_student ON Enrollment (student_id);