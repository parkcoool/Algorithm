with recursive HOURS as (
    select 0 as HOUR
    union all
    select HOUR + 1 as HOUR
    from HOURS
    where HOUR < 23
)

select HOUR, count(ANIMAL_ID) as COUNT
from HOURS h
left join (
    select *, hour(DATETIME) as HOUR
    from ANIMAL_OUTS
) a using (HOUR)
group by HOUR
order by HOUR;