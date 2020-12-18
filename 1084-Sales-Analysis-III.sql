
# Write an SQL query that reports the products that were only sold in spring 2019. That is, between 2019-01-01 and 2019-03-31 inclusive.
# Write your MySQL query statement below

select distinct a.product_id, b.product_name from (
    select product_id from Sales 
    where sale_date BETWEEN '2019-01-01' AND '2019-03-31' 
    and product_id not in (
    select product_id from Sales
    where sale_date < '2019-01-01' or sale_date > '2019-03-31')) a
    left join Product b
    using(product_id)
    order by 1

SELECT sales.product_id, product_name
FROM product
    JOIN sales ON product.product_id = sales.product_id
GROUP BY product_id
HAVING SUM(sale_date BETWEEN '2019-01-01' AND '2019-03-31') = COUNT(sale_date)




------------ explanation --------------

SELECT product_id, SUM(sale_date BETWEEN '2019-01-01' AND '2019-03-31') as a, 
       COUNT(sale_date) as b
       from sales
       group by product_id

SUM(sale_date BETWEEN '2019-01-01' AND '2019-03-31' - product在2019春季出现的次数
COUNT(sale_date) - 出现的总次数
HAVING - 可以有aggregation function