SELECT *
FROM
(
SELECT DepartmentID, Salary
FROM Employees
) SourceTable

PIVOT
(
SUM(Salary)
FOR DepartmentID IN ([1],[2],[3],[4])
) P;
