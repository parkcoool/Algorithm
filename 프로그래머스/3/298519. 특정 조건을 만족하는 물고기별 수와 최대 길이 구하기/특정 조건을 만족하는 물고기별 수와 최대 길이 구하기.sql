with MAPPED_FISH_INFO as (
    select
        ID,
        FISH_TYPE,
        coalesce(LENGTH, 10) as LENGTH
    from FISH_INFO
)

select
    count(*) as FISH_COUNT,
    max(LENGTH) as MAX_LENGTH,
    FISH_TYPE
from MAPPED_FISH_INFO
group by FISH_TYPE
having avg(LENGTH) >= 33
order by FISH_TYPE asc;