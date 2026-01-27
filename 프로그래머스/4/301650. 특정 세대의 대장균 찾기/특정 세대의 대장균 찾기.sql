with recursive generation as (
    select
        ID,
        1 as GENERATION
    from ECOLI_DATA
    where PARENT_ID is NULL
    
    union all
    
    select
        c.ID,
        GENERATION + 1 as GENERATION
    from generation p join ECOLI_DATA c on p.ID = c.PARENT_ID
    where GENERATION < 3
)

select ID from generation where GENERATION = 3 order by ID asc;