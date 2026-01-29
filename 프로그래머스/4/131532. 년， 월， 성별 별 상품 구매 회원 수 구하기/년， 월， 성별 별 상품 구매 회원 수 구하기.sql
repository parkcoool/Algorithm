select
    year(SALES_DATE) as YEAR,
    month(SALES_DATE) as MONTH,
    GENDER,
    count(DISTINCT USER_ID) as USERS
from ONLINE_SALE join USER_INFO using(USER_ID)
where GENDER is not null
group by YEAR, MONTH, GENDER
order by YEAR asc, MONTH asc, GENDER asc;