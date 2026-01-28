select
    CAR_ID,
    if(max(if("2022-10-16" between START_DATE and END_DATE, 1, 0)) = 1, "대여중", "대여 가능") as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
order by CAR_ID desc;