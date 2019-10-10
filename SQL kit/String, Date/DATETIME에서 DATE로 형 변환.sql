-- https://programmers.co.kr/learn/courses/30/lessons/59414

SELECT 
    ANIMAL_ID
    , NAME
    , DATE_FORMAT(DATETIME, GET_FORMAT(DATE, 'ISO')) AS '날짜'
FROM 
    ANIMAL_INS 
ORDER BY 
    ANIMAL_ID
