SELECT department, COUNT(*) AS student_count, AVG(gpa) AS average_gpa
FROM Students
GROUP BY department
HAVING COUNT(*) < 3, 

