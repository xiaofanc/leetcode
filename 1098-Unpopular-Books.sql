# Write your MySQL query statement below

with 
    cte1 as (
    select a.book_id, sum(case when b.dispatch_date between '2018-06-23' and '2019-06-23' then b.quantity else 0 end) as total_n from Books a left join Orders b using(book_id) group by 1)
    

select book_id, name from Books join cte1 using(book_id) where total_n < 10 and available_from < DATE_ADD('2019-06-23', INTERVAL -1 Month)


with 
    cte1 as (
    select a.book_id, 
           sum(case when b.dispatch_date between date_add("2019-06-23", interval -1 year) and "2019-06-23" then b.quantity else 0 end) as total_n 
    from Books a 
    left join Orders b 
    using(book_id) 
    group by 1)
    

select book_id, name 
    from Books 
    join cte1 
    using(book_id) 
    where total_n < 10 and available_from < DATE_ADD('2019-06-23', INTERVAL -1 Month)






