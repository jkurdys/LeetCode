/*
177. Nth Highest Salary
Write an SQL query to report
the nth highest salary from the Employee table. If
there is no nth highest salary, the query should
report null.
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      
          SELECT 
            CASE WHEN count(1) > 0 THEN salary
            ELSE NULL 
            END AS result
          FROM (
              SELECT salary,
                     dense_rank() OVER (ORDER BY salary DESC) AS nth
              FROM employee
              ) AS sub
          WHERE n = nth
  );
END