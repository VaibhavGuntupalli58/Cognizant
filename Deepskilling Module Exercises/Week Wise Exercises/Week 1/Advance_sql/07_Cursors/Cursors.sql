DECLARE @EmployeeID INT,
@FirstName VARCHAR(50),
@LastName VARCHAR(50)
DECLARE EmployeeCursor CURSOR FOR
SELECT EmployeeID,
FirstName,
LastName
FROM Employees
OPEN EmployeeCursor
FETCH NEXT FROM EmployeeCursor
INTO @EmployeeID,@FirstName,@LastName
WHILE @@FETCH_STATUS=0
BEGIN
PRINT CAST(@EmployeeID AS VARCHAR)
+ ' ' + @FirstName
+ ' ' + @LastName
FETCH NEXT FROM EmployeeCursor
INTO @EmployeeID,@FirstName,@LastName
END
CLOSE EmployeeCursor
DEALLOCATE EmployeeCursor


