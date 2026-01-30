with HR_SCORE as (
    select
        e.*,
        avg(SCORE) as SCORE
    from HR_EMPLOYEES e
    join HR_GRADE
    using (EMP_NO)
    group by EMP_NO
)

select
    EMP_NO,
    EMP_NAME,
    (
        case
            when SCORE >= 96 then "S"
            when SCORE >= 90 then "A"
            when SCORE >= 80 then "B"
            else "C"
        end
    ) as GRADE,
    (
        case
            when SCORE >= 96 then SAL * 0.2
            when SCORE >= 90 then SAL * 0.15
            when SCORE >= 80 then SAL * 0.1
            else 0
        end
    ) as BONUS
from HR_SCORE
order by EMP_NO asc;