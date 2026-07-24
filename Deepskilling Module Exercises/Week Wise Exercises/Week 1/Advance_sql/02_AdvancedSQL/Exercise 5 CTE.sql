WITH EmployeeCount AS
(
SELECT DepartmentID,
COUNT(*) AS TotalEmployees
FROM Employees
GROUP BY DepartmentID
)

SELECT *
FROM EmployeeCount
WHERE TotalEmployees > 0;
