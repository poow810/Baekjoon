-- 코드를 작성해주세요

SELECT ROUND(SUM(IFNULL(LENGTH, 10))/COUNT(*), 2) AS AVERAGE_LENGTH FROM FISH_INFO