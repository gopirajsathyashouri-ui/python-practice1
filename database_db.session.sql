DROP TABLE students;
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100),
    email VARCHAR(100),
    age INT
);

INSERT INTO students (student_name, email, age)
VALUES
    ('Ravi Sharma', 'ravi@example.com', 22),
    ('Priya Patel', 'priya@example.com', 21);
SELECT * FROM students;