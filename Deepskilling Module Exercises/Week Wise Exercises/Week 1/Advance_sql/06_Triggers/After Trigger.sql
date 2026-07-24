CREATE TRIGGER trg_AfterSalaryUpdate
ON Employees
AFTER UPDATE
AS
BEGIN
INSERT INTO EmployeeChanges
SELECT d.EmployeeID,
d.Salary,
i.Salary,
GETDATE()
FROM deleted d
JOIN inserted i
ON d.EmployeeID=i.EmployeeID;
END;
