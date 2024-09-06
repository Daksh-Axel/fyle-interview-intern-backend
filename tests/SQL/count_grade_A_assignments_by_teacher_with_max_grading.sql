-- Write query to find the number of grade A's given by the teacher who has graded the most assignments

WITH teacher_and_gradedCount AS (
    SELECT teacher_id, COUNT(id) AS graded_assignments
    FROM assignments
    WHERE state = "GRADED"
    GROUP BY teacher_id
    ORDER BY graded_assignments DESC
    LIMIT 1
)

SELECT COUNT(id) AS Number_of_A 
FROM assignments
WHERE state = "GRADED" AND grade = 'A' AND teacher_id = ( SELECT teacher_id FROM teacher_and_gradedCount)
