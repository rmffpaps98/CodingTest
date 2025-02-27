# 잘 모르겠음
WITH RECURSIVE TMP AS (
    SELECT ID, PARENT_ID, 1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    UNION ALL
    SELECT S.ID, S.PARENT_ID, TMP.GENERATION + 1
    FROM TMP JOIN ECOLI_DATA S
    ON TMP.ID = S.PARENT_ID
)

SELECT COUNT(*) AS COUNT, GENERATION
FROM TMP
WHERE ID NOT IN (
    SELECT DISTINCT PARENT_ID
    FROM TMP
    WHERE PARENT_ID IS NOT NULL
)
GROUP BY GENERATION
ORDER BY GENERATION ASC;