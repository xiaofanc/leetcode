
# Write an SQL query to find the person_name of the last person who will fit in the elevator without exceeding the weight limit. It is guaranteed that the person who is first in the queue can fit in the elevator.

# Write your MySQL query statement below
with cte as (
select *, sum(weight) over (order by turn) as cumulative_sum
from Queue)

select person_name from cte 
where cumulative_sum <= 1000
order by turn desc
limit 1