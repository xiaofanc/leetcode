
# Write an SQL query to find the percentage of immediate orders in the table, rounded to 2 decimal places.

select round(immediate_order_n/total_order_n*100,2) as immediate_percentage
from (
select
    sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) as immediate_order_n,
    count(delivery_id) as total_order_n
from Delivery) a




with cte1 as (select sum(case when order_date = customer_pref_delivery_date then 1 else 0 end) as immediate_order_n from Delivery),
cte2 as (select count(delivery_id) as total_order_n from Delivery)

select round(c1.immediate_order_n/c2.total_order_n*100,2) as immediate_percentage
from cte1 as c1, cte2 as c2
