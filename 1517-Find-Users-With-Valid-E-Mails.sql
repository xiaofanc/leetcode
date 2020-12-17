# Write an SQL query to find the users who have valid emails.

select * from Users
where mail REGEXP '^[A-Za-z][A-Za-z0-9\.\_\-]*@leetcode.com$'

select * from Users
where mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode.com$'

SELECT * FROM Users WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$')

