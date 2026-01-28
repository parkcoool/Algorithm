select
    b.AUTHOR_ID,
    AUTHOR_NAME,
    b.CATEGORY,
    sum(PRICE * SALES) as TOTAL_SALES
from BOOK b
join AUTHOR a on b.AUTHOR_ID = a.AUTHOR_ID
join (
    select *
    from BOOK_SALES
    where year(SALES_DATE) = 2022 and month(SALES_DATE) = 1
) s
on b.BOOK_ID = s.BOOK_ID
group by AUTHOR_ID, CATEGORY
order by AUTHOR_ID asc, CATEGORY desc;