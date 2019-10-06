-- https://programmers.co.kr/learn/courses/30/lessons/59412

SELECT 
    HOUR(DATETIME)
    , COUNT(HOUR(DATETIME))
FROM 
    ANIMAL_OUTS
WHERE 
    HOUR(DATETIME) >= 9
    AND HOUR(DATETIME) <= 19
GROUP BY 
    HOUR(DATETIME)
