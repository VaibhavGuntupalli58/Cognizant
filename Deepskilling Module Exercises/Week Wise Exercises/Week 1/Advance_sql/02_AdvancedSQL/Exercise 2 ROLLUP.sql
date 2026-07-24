SELECT DepartmentID,
SUM(Salary) AS TotalSalary
FROM Employees
GROUP BY ROLLUP(DepartmentID);