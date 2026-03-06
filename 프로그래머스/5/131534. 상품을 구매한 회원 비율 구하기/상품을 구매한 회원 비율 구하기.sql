with USER as (
    select USER_ID
    from USER_INFO
    where year(JOINED) = 2021
),

SALE as (
    select
        USER_ID,
        year(SALES_DATE) as YEAR,
        month(SALES_DATE) as MONTH,
        ONLINE_SALE_ID
    from ONLINE_SALE
),

PURCHASED_USER as (
    select
        USER_ID,
        YEAR,
        MONTH
    from USER
    join SALE using (USER_ID)
),

PURCHASED_COUNT as (
    select 
        YEAR,
        MONTH,
        count(distinct USER_ID) as PURCHASED_USERS
    from PURCHASED_USER
    group by YEAR, MONTH
)

select
    YEAR,
    MONTH,
    PURCHASED_USERS,
    round(
        PURCHASED_USERS / (select count(*) from USER),
        1
    ) as PURCHASED_RATIO
from PURCHASED_COUNT
order by YEAR asc, MONTH asc;