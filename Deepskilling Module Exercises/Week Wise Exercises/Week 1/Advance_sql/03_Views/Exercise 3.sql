CREATE VIEW vw_EmployeeAnnualSalary AS
SELECT EmployeeID,
Salary*12 AS AnnualSalary
FROM Employees;
