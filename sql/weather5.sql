/*
Enter your query here.
*/
select CITY, length(CITY) from station order by length(CITY), city limit 1;
select CITY, length(CITY) from station order by length(CITY) desc, city limit 1;

/*
Enter your query here.
*/
SELECT DISTINCT city FROM station WHERE city REGEXP "^[aeiou].*";
