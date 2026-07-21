-- Last updated: 7/21/2026, 7:09:25 PM
# Write your MySQL query statement below
SELECT email from Person
group by email
having count(email) > 1;