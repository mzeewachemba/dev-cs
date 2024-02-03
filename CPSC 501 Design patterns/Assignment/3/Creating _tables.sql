USE [StudentDB_1174066]
GO

--SELECT [StudentId]
--      ,[FirstName]
--      ,[LastName]
--      ,[Address]
--      ,[City]
--      ,[State]
--      ,[Cellphone]

--  FROM [dbo].[Students]

--INSERT INTO [dbo].[Students] 

--	   ([StudentId]
--      ,[FirstName]
--      ,[LastName]
--      ,[Address]
--      ,[City]
--      ,[State]
--      ,[Cellphone])

--VALUES
--(123100, 'Bill', 'Baker', '100 Main Street', 'Bridgeport', 'CT', '555-1213'),
--(123101, 'Sally', 'Simpson', '50 Pine Street', 'Milford', 'CT', '557-1214');


--INSERT INTO [dbo].[Courses ] 

--	   ([CourseNum]
--      ,[CourseName]
--      ,[Description]
--      ,[Credits])

--VALUES
--('CPSC 501', 'OOP with D', NULL, 3),
--('CPSC 502', 'Algorithms', NULL, 3),
--('CPSC 555', 'Web App Dev', NULL, 3);

INSERT INTO [dbo].[Enrollments  ] 

	   ([StudentId]
      ,[CourseNum])

VALUES
(123100, 'CPSC 555'),
(123101, 'CPSC 501'),
(123101, 'CPSC 502');
GO


