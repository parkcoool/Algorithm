select distinct(CAR_ID)
from CAR_RENTAL_COMPANY_CAR
join CAR_RENTAL_COMPANY_RENTAL_HISTORY
using (CAR_ID)
where CAR_TYPE = "세단"
and month(START_DATE) = 10
order by CAR_ID desc;