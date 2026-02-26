select
    ID,
    (
        CASE
        WHEN SIZE_RANK <= 0.25 THEN "CRITICAL"
        WHEN SIZE_RANK <= 0.5 THEN "HIGH"
        WHEN SIZE_RANK <= 0.75 THEN "MEDIUM"
        ELSE "LOW"
        END
    ) as COLONY_NAME
from ECOLI_DATA e
join (
    SELECT
        ID,
        PERCENT_RANK() over (order by SIZE_OF_COLONY desc) as SIZE_RANK
    from ECOLI_DATA
) r
using (ID);