with TOTAL as (
    select * from FIRST_HALF
    union all
    select * from JULY
),
TOTAL_ORDER as (
    select
        FLAVOR,
        SUM(TOTAL_ORDER) as TOTAL_ORDER
    from TOTAL
    group by FLAVOR
)

select FLAVOR
from TOTAL_ORDER
order by TOTAL_ORDER desc
limit 3;