SELECT EmployeeID,
dbo.fn_CalculateAnnualSalary(Salary)
AS AnnualSalary
FROM Employees;
