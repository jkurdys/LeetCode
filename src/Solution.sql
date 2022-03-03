/*
177. Nth Highest SalaryWrite an SQL query to report
the nth highest salary from the Employee table. If
there is no nth highest salary, the query should
report null.
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      
          select salary
          from (
              select salary,
                     row_number() over (order by salary desc) as nth
              from employee
              ) as sub
          where n = nth
  );
END