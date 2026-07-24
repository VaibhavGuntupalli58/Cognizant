CREATE PROCEDURE sp_InsertEmployee
@FirstName VARCHAR(50),
@LastName VARCHAR(50),
@DepartmentID INT,
@Salary DECIMAL(10,2),
@JoinDate DATE

AS
BEGIN

INSERT INTO Employees
VALUES
(5,@FirstName,@LastName,
@DepartmentID,@Salary,@JoinDate);

END;

