
# whether three line segments could possibly form a triangle.

select
x,y,z,
case when x+y <= z or x+z <= y or y+z <= x then "No" else "Yes" end as triangle
from triangle
