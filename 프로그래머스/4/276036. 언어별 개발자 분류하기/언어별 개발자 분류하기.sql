select
    (
        case
            when FRONTEND and PYTHON then "A"
            when CSHARP then "B"
            when FRONTEND then "C"
            else null
        end
    ) as GRADE,
    ID,
    EMAIL
from (
    select
        max(if(s.CATEGORY = "Front End", 1, 0)) as FRONTEND,
        max(if(s.NAME = "C#", 1, 0)) as CSHARP,
        max(if(s.NAME = "Python", 1, 0)) as PYTHON,
        ID,
        EMAIL
    from DEVELOPERS d
    join SKILLCODES s
    on d.SKILL_CODE & s.CODE > 0
    group by ID, EMAIL
) a
having GRADE is not null
order by GRADE asc, ID asc;