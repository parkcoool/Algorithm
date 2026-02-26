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
    on g.ID = e.PARENT_ID
    where GENERATION <= 3
)

select ID
from GENERATION_DATA
where GENERATION = 3
order by ID asc;