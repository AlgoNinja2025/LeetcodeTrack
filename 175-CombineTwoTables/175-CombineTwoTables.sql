-- Last updated: 7/21/2026, 7:09:35 PM
# Write your MySQL query statement below
SELECT
    p.firstName,
    p.lastName,
    a.city,
    a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId;