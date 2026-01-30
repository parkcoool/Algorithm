select
    DEPT_ID,
    DEPT_NAME_EN,
    round(avg(SAL)) as AVG_SAL
from HR_DEPARTMENT
join HR_EMPLOYEES
using (DEPT_ID)
group by DEPT_ID
order by AVG_SAL desc;