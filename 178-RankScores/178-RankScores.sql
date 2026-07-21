-- Last updated: 7/21/2026, 7:09:31 PM
# Write your MySQL query statement below
select S.score, count(S2.Score) as `rank` from SCORES S,
(select distinct SCORE from SCORES) S2
where S.SCORE<=S2.SCORE
group by S.ID
order by S.SCORE desc;