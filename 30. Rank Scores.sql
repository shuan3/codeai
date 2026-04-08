select  score, rnk as "rank" from (
select id, score, dense_rank() over(order by score desc) as rnk from Scores) as a
order by rnk asc




SELECT score, DENSE_RANK() OVER(ORDER BY score DESC) as `rank`
FROM Scores
ORDER BY score DESC;