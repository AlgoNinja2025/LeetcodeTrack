-- Last updated: 7/21/2026, 7:09:28 PM
# Write your MySQL query statement below
select e1.name as Employee
from employee e1 join employee e2
on e1.managerid=e2.id and e1.salary>e2.salary;