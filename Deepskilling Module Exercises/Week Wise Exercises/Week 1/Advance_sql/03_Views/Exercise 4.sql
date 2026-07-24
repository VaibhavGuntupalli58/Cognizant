CREATE VIEW vw_EmployeeReport AS
SELECT
e.EmployeeID,
e.FirstName+' '+e.LastName AS FullName,
d.DepartmentName,
Salary*12 AS AnnualSalary,
(Salary*12)*0.10 AS Bonus

FROM Employees e
JOIN Departments d
ON e.DepartmentID=d.DepartmentID;
