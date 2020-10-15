# Write your MySQL query statement below
# Given two tables as below, write a query to display the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.

# Write your MySQL query statement below
select
b.pay_month,
b.department_id,
case when b.avg_dpt > c.avg_comp then "higher"
     when b.avg_dpt = c.avg_comp then "same"
     else "lower"
     end as comparison
from (
    select 
    substr(pay_date, 1, 7) as pay_month,
    department_id,
    avg(amount) as avg_dpt
    from salary s
    join employee e
    on s.employee_id = e.employee_id
    group by 1,2) b
join (
    select distinct 
    substr(pay_date, 1, 7) as pay_month,
    avg(amount) as avg_comp
    from salary
    group by 1) c
on b.pay_month = c.pay_month


solution:
select department_salary.pay_month, department_id,
case
  when department_avg>company_avg then 'higher'
  when department_avg<company_avg then 'lower'
  else 'same'
end as comparison
from
(
  select department_id, avg(amount) as department_avg, date_format(pay_date, '%Y-%m') as pay_month
  from salary join employee on salary.employee_id = employee.employee_id
  group by department_id, pay_month
) as department_salary
join
(
  select avg(amount) as company_avg,  date_format(pay_date, '%Y-%m') as pay_month from salary group by date_format(pay_date, '%Y-%m')
) as company_salary
on department_salary.pay_month = company_salary.pay_month
;
    








    





