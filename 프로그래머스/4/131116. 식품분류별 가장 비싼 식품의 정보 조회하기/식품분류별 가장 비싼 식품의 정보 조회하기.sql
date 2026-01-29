select a.CATEGORY, a.PRICE, a.PRODUCT_NAME
from FOOD_PRODUCT a
join (
    select CATEGORY, MAX(PRICE) as MAX_PRICE
    from FOOD_PRODUCT
    where CATEGORY in ("과자", "국", "김치", "식용유")
    group by CATEGORY
) b
using (CATEGORY)
where a.PRICE = b.MAX_PRICE
order by PRICE desc;