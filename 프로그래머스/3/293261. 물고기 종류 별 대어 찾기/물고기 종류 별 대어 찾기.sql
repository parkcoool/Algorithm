select ID, FISH_NAME, LENGTH
from FISH_INFO a
join FISH_NAME_INFO b
on a.FISH_TYPE = b.FISH_TYPE
join (
    select FISH_TYPE, max(LENGTH) as MAX_LENGTH
    from FISH_INFO
    group by FISH_TYPE
) c
on a.FISH_TYPE = c.FISH_TYPE
where LENGTH = MAX_LENGTH
order by ID;