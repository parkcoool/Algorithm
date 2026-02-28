with SALE_AMOUNT as (
    select
        PRODUCT_ID,
        sum(AMOUNT) as AMOUNT,
        PRODUCE_DATE
    from FOOD_ORDER
    where PRODUCE_DATE between "2022-05-01" and "2022-05-31"
    group by PRODUCT_ID
)

select
    PRODUCT_ID,
    PRODUCT_NAME,
    PRICE * AMOUNT as TOTAL_SALES
from FOOD_PRODUCT
join SALE_AMOUNT
using (PRODUCT_ID)
order by TOTAL_SALES desc, PRODUCT_ID asc;