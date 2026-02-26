with recursive GENERATION_DATA as (
    select
        1 as GENERATION,
        ID
    from ECOLI_DATA
    where PARENT_ID is null
    
    union all
    
    select
        GENERATION + 1 as GENERATION,
        e.ID as ID
    from GENERATION_DATA g
    join ECOLI_DATA e
    on e.PARENT_ID = g.ID
),

COUNT_DATA as (
    select
        PARENT_ID,
        count(*) as COUNT
    from ECOLI_DATA
    group by PARENT_ID
)

select
    COUNT(*) as COUNT,
    GENERATION
from ECOLI_DATA e
join GENERATION_DATA g
using (ID)
left join COUNT_DATA c
on e.ID = c.PARENT_ID
where COUNT is null
group by GENERATION
order by GENERATION asc;