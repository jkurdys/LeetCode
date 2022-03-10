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

/*
178. Rank Scores

Write an SQL query to rank the scores. The ranking
should be calculated according to the following rules:

    The scores should be ranked from the highest to
    the lowest.
    If there is a tie between two scores, both should
    have the same ranking.
    After a tie, the next ranking number should be the
    next consecutive integer value. In other words,
    there should be no holes between ranks.

Return the result table ordered by score in descending
order.
*/

SELECT score,
       DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM scores;