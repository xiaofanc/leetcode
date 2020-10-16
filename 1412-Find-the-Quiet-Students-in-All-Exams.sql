# Write your MySQL query statement below
with score as (
select 
    exam_id,
    max(score) as mscore
    from exam
    group by exam_id

    union

    select 
    exam_id, 
    min(score) as mscore
    from exam
    group by exam_id
)

select distinct e.student_id, s.student_name from exam e left join student s 
on e.student_id = s.student_id
where e.student_id not in (
    select e.student_id from exam e inner join score s 
    on e.exam_id = s.exam_id and e.score = s.mscore )
and e.student_id in (
    select distinct student_id from exam)
order by 1

# using window function
select distinct s.student_id, s.student_name from student s left join exam e
on e.student_id = s.student_id
where e.student_id is not null and
e.student_id not in (
    select student_id from 

    (select 
     student_id, 
     rank() over(partition by exam_id order by score)as grade_asc,  
     rank() over(partition by exam_id order by score desc)as grade_desc
     from exam
    )a
     where a.grade_asc = 1 or a.grade_desc = 1)
     
order by 1