with recursive tree as (
    select
        id,
        1 as generation
    from ecoli_data
    where parent_id is null
    
    union all
    
    select
        b.id,
        generation + 1 as generation
    from tree a
    join ecoli_data b on a.id = b.parent_id
)

select count(a.id) as COUNT, generation as GENERATION
from ecoli_data a
left join ecoli_data b on a.id = b.parent_id
join tree on a.id = tree.id
where b.id is null
group by generation
order by generation;