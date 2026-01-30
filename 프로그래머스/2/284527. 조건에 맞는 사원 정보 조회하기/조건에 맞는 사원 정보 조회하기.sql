select
    sum(SCORE) as SCORE,
    EMP_NO,
    EMP_NAME,
    POSITION,
    EMAIL
from HR_EMPLOYEES 
join HR_GRADE
using (EMP_NO)
where YEAR = 2022
group by EMP_NO
order by SCORE desc
LIMIT 1;