# The winner in each group is the player who scored the maximum total points within the group. In the case of a tie, the lowest player_id wins.

# Write your MySQL query statement below

with cte1 as (select distinct first_player, sum(first_score) as score_1 from Matches group by 1), 
cte2 as (select distinct second_player, sum(second_score) as score_2 from Matches group by 1), 
cte3 as (
    select *,
    row_number() OVER (PARTITION BY group_id ORDER BY total_score desc, player_id) as row_num
    from (
        select player_id, group_id, 
        coalesce(c1.score_1, 0) +  coalesce(c2.score_2, 0) as total_score
        from Players p left join cte1 as c1 on p.player_id = c1.first_player 
                       left join cte2 as c2 on p.player_id = c2.second_player 
         ) a)

select group_id, player_id from cte3
where row_num = 1