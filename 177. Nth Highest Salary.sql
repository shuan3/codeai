CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select  salary from
     ( select DENSE_RANK() over (order by salary desc) as ran, salary, id from Employee) as a
      where ran=N
      limit 1

  );
END


# rank vs dense_rank vs row_number
# rank: 1, 2, 2, 4
# dense_rank: 1, 2, 2, 3
# row_number: 1, 2, 3, 4
# https://www.mssqltips.com/sqlservertip/7657/ranking-functions-sql-row-number-rank-dense-rank-ntile/


CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      with cte as ( select salary, 
      dense_rank() over(order by salary desc)as rnk
      from employee)
      select max(distinct salary) as  getNthHighestSalary
      from cte 
      where rnk=n

  );
END