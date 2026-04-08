# Write your MySQL query statement below
select Department , name as "Employee",salary as "Salary" from (
select a.id ,a.name,b.name as "Department",a.salary, rank() over(partition by a.departmentId order by a.salary desc) as rnk 
from Employee as a
join Department as b 
on a.departmentId=b.id
group by b.id,a.name
) as a
where rnk =1








SELECT Department,
    Employee,
    Salary
FROM(
    Select
    d.name as Department,
    e.name as Employee,
    e.salary as Salary,
    Dense_rank() Over(partition by d.id
    order by e.salary desc) as rnk
    From Employee e
    Join Department d
        on e.departmentid=d.id
)t
WHERE rnk=1;