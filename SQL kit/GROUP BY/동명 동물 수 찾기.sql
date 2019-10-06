-- https://programmers.co.kr/learn/courses/30/lessons/59041

SELECT 
    NAME
    , COUNT(NAME)
FROM 
    ANIMAL_INS 
WHERE 
    NAME IS NOT NULL
GROUP BY 
    NAME
HAVING 
    COUNT(NAME) > 1
