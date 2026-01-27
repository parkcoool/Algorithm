select p.ID as ID, coalesce(c.COUNT, 0) as CHILD_COUNT
from ECOLI_DATA p left join (
    select PARENT_ID, count(*) as COUNT
    from ECOLI_DATA
    group by PARENT_ID
) c on p.ID = c.PARENT_ID
order by ID asc;