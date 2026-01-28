select
    YEAR,
    MAX_SIZE - SIZE_OF_COLONY as YEAR_DEV,
    ID
from ECOLI_DATA a
join (
    select
        year(DIFFERENTIATION_DATE) as YEAR,
        max(SIZE_OF_COLONY) as MAX_SIZE
    from ECOLI_DATA
    group by YEAR
) b
on year(a.DIFFERENTIATION_DATE) = b.year
order by YEAR asc, YEAR_DEV asc;