CREATE TRIGGER trg_PreventDelete
ON Employees
INSTEAD OF DELETE
AS
BEGIN
PRINT 'Deletion Not Allowed'
END;