
{"headers":{"Actions":["user_id","post_id","action_date","action","extra"],"Removals":["post_id","remove_date"]},"rows":{
"Actions":[[2,2,"2019-07-04","view",null],
           [2,2,"2019-07-04","report","racism"],
           [3,4,"2019-07-04","view",null],
           [3,4,"2019-07-04","report","spam"],    0%
           [4,3,"2019-07-02","view",null],
           [4,3,"2019-07-02","report","spam"],    100%
           [5,2,"2019-07-07","view",null],
           [5,2,"2019-07-07","report","racism"],
           [5,5,"2019-07-07","view",null],
           [5,5,"2019-07-07","report","spam"]],   0%

"Removals":[[2,"2019-07-20"],
            [3,"2019-07-18"]]}}

# average = 33.33%


{"headers":{"Actions":["user_id","post_id","action_date","action","extra"],"Removals":["post_id","remove_date"]},"rows":{
"Actions":[ [1,1,"2019-07-01","view",null],
            [1,1,"2019-07-01","like",null],
            [1,1,"2019-07-01","share",null],  
            [2,2,"2019-07-04","view",null],
            [2,2,"2019-07-04","report","spam"], Y  
            [3,4,"2019-07-04","view",null],
            [3,4,"2019-07-04","report","spam"],    50%
            [4,3,"2019-07-02","view",null],
            [4,3,"2019-07-02","report","spam"], Y  100%
            [5,2,"2019-07-03","view",null],
            [5,2,"2019-07-03","report","racism"],
            [5,5,"2019-07-03","view",null],
            [5,5,"2019-07-03","report","racism"]],
"Removals":[[2,"2019-07-20"],
            [3,"2019-07-18"]]}}

# average = 75.00%

# Write your MySQL query statement below

# Write your MySQL query statement below

with cte1 as(
    select 
    distinct post_id,
    (case when remove_date is null then 'F' else 'T' end) as spam,
    action_date
    from Actions left join Removals
    using(post_id)
    where extra = "spam" and action = 'report'
    ),
    
    cte2 as (
    select  cte1.action_date, 
            sum(case when cte1.spam = 'T' then 1 else 0 end) / count(*) as pct
            from cte1
            group by 1
    )
    
select round(avg(pct)*100,2) as average_daily_percent from cte2





