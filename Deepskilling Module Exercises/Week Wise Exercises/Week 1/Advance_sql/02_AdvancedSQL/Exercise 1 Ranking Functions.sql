SELECT *,
ROW_NUMBER() OVER
(PARTITION BY DepartmentID ORDER BY Salary DESC) AS RowNum,

RANK() OVER
(PARTITION BY DepartmentID ORDER BY Salary DESC) AS RankNum,

DENSE_RANK() OVER
(PARTITION BY DepartmentID ORDER BY Salary DESC) AS DenseRankNum

FROM Employees;