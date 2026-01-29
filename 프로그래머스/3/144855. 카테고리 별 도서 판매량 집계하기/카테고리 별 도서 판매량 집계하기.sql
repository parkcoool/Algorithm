select CATEGORY, sum(SALES) as TOTAL_SALES
from BOOK join BOOK_SALES using (BOOK_ID)
where SALES_DATE LIKE "2022-01%"
group by CATEGORY
order by CATEGORY asc;