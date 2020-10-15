select employee_id from Employees where manager_id in (
    select employee_id from Employees where manager_id in (
        select
        employee_id
        from Employees
        where manager_id = 1 and employee_id != 1) 
    )
    
union

select employee_id from Employees where manager_id in (
    select
    employee_id
    from Employees
    where manager_id = 1 and employee_id != 1) 

union 

select
employee_id
from Employees
where manager_id = 1 and employee_id != 1

solution:
select e1.employee_id from employees e1 
left join employees e2 on e1.manager_id = e2.employee_id
left join employees e3 on e2.manager_id = e3.employee_id
where e3.manager_id = 1 and e1.employee_id != 1