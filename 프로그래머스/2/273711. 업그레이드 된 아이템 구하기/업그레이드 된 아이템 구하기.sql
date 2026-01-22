SELECT
    info.ITEM_ID, ITEM_NAME, RARITY
FROM
    ITEM_INFO info JOIN ITEM_TREE tree ON info.ITEM_ID = tree.ITEM_ID
WHERE
    (
        SELECT
            RARITY
        FROM
            ITEM_INFO
        WHERE
            ITEM_ID = PARENT_ITEM_ID
    ) = "RARE"
ORDER BY
    ITEM_ID DESC;