CREATE TABLE AuditLog
(
LogID INT IDENTITY PRIMARY KEY,
Action VARCHAR(100),
ErrorMessage VARCHAR(4000),
ActionDate DATETIME DEFAULT GETDATE()
);
CREATE PROCEDURE AddEmployee
@EmployeeID INT,
@FirstName VARCHAR(50),
@LastName VARCHAR(50),
@Salary DECIMAL(10,2),
@DepartmentID INT
AS
BEGIN TRY
INSERT INTO Employees
VALUES(@EmployeeID,@FirstName,
@LastName,@DepartmentID,
@Salary,GETDATE());
END TRY
BEGIN CATCH
INSERT INTO AuditLog
(Action,ErrorMessage)
VALUES
('Insert Failed',ERROR_MESSAGE());
END CATCH   
