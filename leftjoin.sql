SELECT e.emp_name, d.department_name
FROM employees1 AS e
LEFT JOIN departments1  AS d
ON e.department_id = d.department_id;