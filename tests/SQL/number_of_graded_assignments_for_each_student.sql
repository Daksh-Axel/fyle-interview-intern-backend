-- Write query to get number of graded assignments for each student:
SELECT student_id, COUNT(id) AS Graded_Assignments
FROM assignments
WHERE state = "GRADED"
GROUP BY student_id;