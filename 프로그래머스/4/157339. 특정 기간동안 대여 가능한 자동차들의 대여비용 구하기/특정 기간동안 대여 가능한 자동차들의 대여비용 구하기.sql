with CAR as (
    select CAR_ID, CAR_TYPE, DAILY_FEE
    from CAR_RENTAL_COMPANY_CAR
    where CAR_TYPE in ("세단", "SUV")
),

HISTORY as (
    select CAR_ID, HISTORY_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE between "2022-11-01" and "2022-11-30"
    or END_DATE between "2022-11-01" and "2022-11-30"
    or START_DATE < "2022-11-01" and END_DATE > "2022-11-30"
),

DISCOUNT as (
    select CAR_TYPE, CAST(DISCOUNT_RATE as unsigned) as DISCOUNT_RATE
    from CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    where DURATION_TYPE = "30일 이상"
)

select
    CAR_ID,
    CAR_TYPE,
    FLOOR(DAILY_FEE * 30 * (100 - DISCOUNT_RATE) * 0.01) as FEE
from CAR
left join HISTORY using (CAR_ID)
join DISCOUNT using (CAR_TYPE)
group by CAR_ID
having count(HISTORY_ID) = 0
and FEE between 500000 and 2000000
order by FEE desc, CAR_TYPE asc, CAR_ID desc;