-- 코드를 입력하세요
SELECT NAME, count(name) as count 
from ANIMAL_INS  
group by NAME 
ORDER BY NAME