select concat("/home/grep/src/", BOARD_ID, "/", FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
from USED_GOODS_FILE
where BOARD_ID = (
    select BOARD_ID
    from USED_GOODS_BOARD
    order by VIEWS desc
    limit 1
)
order by FILE_ID desc;