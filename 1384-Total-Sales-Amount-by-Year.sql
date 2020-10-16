# MS SQL SERVER 
#SELECT DATEDIFF(year, '2017/08/25', '2011/08/25') AS DateDiff;

#set @miny=(select min(year(period_start)) from sales), @maxy=(select max(year(period_end)) from sales);
#https://dev.mysql.com/doc/refman/8.0/en/with.html

# method 1
declare @miny int=(select min(year(period_start)) from sales);

declare @maxy int=(select max(year(period_end)) from sales);

with myear as (
select @miny as year_id
    union all
select year_id+1 
    from myear
    where year_id<@maxy
)

select s.product_id, product_name, cast(myear.year_id as varchar) report_year, (datediff(d,case when concat(myear.year_id,'-01-01')>s.period_start then concat(myear.year_id,'-01-01') else s.period_start end, case when concat(myear.year_id,'-12-31')<s.period_end then concat(myear.year_id,'-12-31') else s.period_end end)+1)*s.average_daily_sales total_amount
from sales s
join myear
on myear.year_id between year(s.period_start) and year(s.period_end)
join product
on s.product_id=product.product_id
order by 1,3

# method 2
WITH cte AS(

    SELECT product_id, 
            '2018' AS report_year,
            CASE
            WHEN period_start >= '2019-01-01' THEN 0
            WHEN period_end < '2019-01-01' AND period_start<'2019-01-01' THEN  DATEDIFF(period_end, period_start)+1
            ELSE DATEDIFF('2019-01-01', period_start)
            END AS days_in_year,
            average_daily_sales
    FROM Sales 
    
    UNION 
    
    SELECT product_id, 
            '2019' AS report_year,
            CASE
            WHEN period_start >='2020-01-01' THEN 0
            WHEN period_end < '2020-01-01' AND period_start > '2018-12-31' THEN  DATEDIFF(period_end, period_start)+1
            WHEN period_end < '2020-01-01' AND period_start <= '2018-12-31' THEN DATEDIFF(period_end, '2018-12-31')
            WHEN period_end >= '2020-01-01' AND period_start > '2018-12-31' THEN  DATEDIFF('2020-01-01', period_start)
            ELSE DATEDIFF('2020-01-01', '2019-01-01')
            END AS days_in_year,
            average_daily_sales

    FROM Sales 

    UNION 
    
    SELECT product_id, 
            '2020' AS report_year,
            CASE
            WHEN period_start >= '2020-01-01' THEN  DATEDIFF(period_end, period_start)+1
            WHEN period_end <'2020-01-01' THEN 0
            ELSE DATEDIFF(period_end, '2019-12-31')
            END AS days_in_year,
            average_daily_sales
    FROM Sales 
)

SELECT c.product_id, 
        p.product_name,  
        c.report_year,
        c.days_in_year*c.average_daily_sales AS total_amount
FROM cte c
JOIN Product p ON c.product_id = p.product_id 
WHERE c.days_in_year>0
ORDER BY 1, 3