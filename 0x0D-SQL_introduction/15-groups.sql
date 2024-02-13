-- lists number of records with the same score
USE hbtn_0c_0;
SELECT score, COUNT(*) AS number 
FROM second_table
GROUP BY score
ORDER BY COUNT(*) DESC;