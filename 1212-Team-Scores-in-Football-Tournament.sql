# Write an SQL query that selects the team_id, team_name and num_points of each team in the tournament after all described matches.

# Write your MySQL query statement below
with cte as (
    select *, case when host_goals > guest_goals then 3 
                   when host_goals = guest_goals then 1
                   else 0 end as host_score,
              case when host_goals > guest_goals then 0 
                   when host_goals = guest_goals then 1
                   else 3 end as guest_score
    from Matches),
    
cte1 as (
    select distinct host_team, sum(host_score) as total_host_score from cte group by 1),

cte2 as (
    select distinct guest_team, sum(guest_score) as total_guest_score from cte group by 1)

select team_id, team_name, coalesce(c1.total_host_score, 0) + coalesce(c2.total_guest_score, 0) as num_points
from Teams as t left join cte1 c1 on t.team_id = c1.host_team
                left join cte2 c2 on t.team_id = c2.guest_team
order by 3 desc, team_id


WITH Points AS
(SELECT host_team as team,
CASE WHEN host_goals > guest_goals THEN 3
     WHEN host_goals = guest_goals THEN 1
     ELSE 0 
     END AS points
FROM Matches

UNION ALL

SELECT guest_team as team,
CASE WHEN host_goals < guest_goals THEN 3
     WHEN host_goals = guest_goals THEN 1
     ELSE 0 
     END AS points
FROM Matches )

SELECT team_id, team_name, SUM(ifnull(points,0)) AS num_points
FROM Teams T 
LEFT JOIN Points P
ON team = team_id
GROUP BY team_id
ORDER BY num_points DESC, team_id
