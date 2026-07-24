CREATE TABLE EmployeeChanges
(
ID INT IDENTITY,
EmployeeID INT,
OldSalary DECIMAL(10,2),
NewSalary DECIMAL(10,2),
ChangeDate DATETIME
);