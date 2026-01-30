select
    count(*) as FISH_COUNT,
    FISH_NAME
from FISH_INFO
join FISH_NAME_INFO
using (FISH_TYPE)
group by FISH_NAME
order by FISH_COUNT desc;