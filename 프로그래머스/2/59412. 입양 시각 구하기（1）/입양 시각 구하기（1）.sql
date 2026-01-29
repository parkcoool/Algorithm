select hour(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS
where hour(DATETIME) between 9 and 19
group by HOUR
order by HOUR;