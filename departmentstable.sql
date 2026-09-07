CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    department_id INT,
    manager_id INT,
    CONSTRAINT fk_employees_department
        FOREIGN KEY (department_id)
        REFERENCES departments(department_id))