select count(*) as FISH_COUNT
from FISH_INFO f
join FISH_NAME_INFO n
using (FISH_TYPE)
where FISH_NAME in ("BASS", "SNAPPER");