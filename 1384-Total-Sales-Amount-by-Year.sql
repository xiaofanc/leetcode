# MS SQL SERVER 
#SELECT DATEDIFF(year, '2017/08/25', '2011/08/25') AS DateDiff;

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
