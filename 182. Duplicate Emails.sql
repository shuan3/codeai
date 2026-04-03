select email from(
select email, count(*) from Person
group by email
having count(*)>1
) as a



SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;


select email from Person
group by email
having count(*)>1