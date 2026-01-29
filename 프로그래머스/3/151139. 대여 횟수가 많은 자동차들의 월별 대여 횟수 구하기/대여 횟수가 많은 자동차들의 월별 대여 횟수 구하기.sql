select
    month(START_DATE) as MONTH,
    a.CAR_ID,
    count(*) as RECORDS
from
    (select CAR_ID, count(*) as TOTAL_RECORDS
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE between "2022-08-01" and "2022-10-31"
    group by CAR_ID
    having TOTAL_RECORDS >= 5) a
join CAR_RENTAL_COMPANY_RENTAL_HISTORY using(CAR_ID)
where START_DATE between "2022-08-01" and "2022-10-31"
group by a.CAR_ID, MONTH
having RECORDS > 0
order by MONTH asc, a.CAR_ID desc;