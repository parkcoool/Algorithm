with MONTHLY_FISH_INFO as (
    select
        *,
        month(TIME) as MONTH
    from FISH_INFO
)

select
    count(*) as FISH_COUNT,
    MONTH
from MONTHLY_FISH_INFO
group by MONTH
order by MONTH asc;