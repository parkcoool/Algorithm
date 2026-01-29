select FOOD_TYPE, REST_ID, REST_NAME, FAVORITES
from (
    select
        *,
        max(FAVORITES) over (partition by FOOD_TYPE) as MAX_FAVORITES 
    from REST_INFO
) a
where FAVORITES = MAX_FAVORITES
order by FOOD_TYPE desc;