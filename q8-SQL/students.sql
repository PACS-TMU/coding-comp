-- Do not edit the following
DROP DATABASE students_db;
CREATE DATABASE students_db;
USE students_db;
-- Edit after this comment

-- DO NOT EDIT THE FOLLOWING ONE (1) LINE
DROP TABLE IF EXISTS students;

-- Create a table to store student ids and names
CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  name CHAR(50) NOT NULL
);

-- DO NOT EDIT THE FOLLOWING ONE (1) LINE
DROP TABLE IF EXISTS student_details;

-- Create a table that adds additional info to the students on their unique student id and references the student table
CREATE TABLE student_details(
    id INTEGER PRIMARY KEY,
    gender CHAR(15),
    major CHAR(50),
    coop BIT NOT NULL,
    FOREIGN KEY (id) REFERENCE students(id)
);

-- insert some people into the students table with unique ids
INSERT INTO students VALUES (1 'Ryan');
INSERT INTO student VALUES (2, 'Joanna');
INSERT INTO students VALUES (3, 'Mo');
INSERT INTO student VALUES (4, 'William');
INSERT INTO students VALUES (5, Bennie);

-- insert additional details to the students using their unique ids to match the details to the correct student
INSERT INTO student_details VALUES (1, Male', 'Art', 0);
INSERT INTO student_details VALUES (2, 'Female', 'Comp Sci', 1);
INSERT INTO students_details VALUES (3, 'Male', 'Creative Industries', 1);
INSERT INTO students_detail VALUES (4, 'Male', 'Marketing', 0);
INSERT INTO student_detils VALUES (4, 'Female', 'Comp Sci', 0);

--Listing all the Comp Sci students with their id, name and major only
SELECT students.id, students.name, student_details.major FROM students;
INNER JOIN student_details ON students.id=students.id
WHERE student_details.major = 'Comp Sci';