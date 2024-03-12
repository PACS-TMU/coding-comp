-- DO NOT TOUCH 

-- DO NOT TOUCH
IF EXISTS DROP TABLE World;

-- DO NOT TOUCH
CREATE TABLE World
(
    name varchar,
    continent varchar,
    area int,
    population int,
    gdp bigint
);

-- DO NOT TOUCH
INSERT INTO World
VALUES
("Afghanistan", "Asia", 652230, 25500100, 20343000000),
("Albania", "Europe", 28748, 2831741, 12960000000),
("Algeria", "Africa",2381741, 37100000, 188681000000),
("Andorra", "Europe",468, 78115, 3712000000),
("Angola", "Africa", 1246700, 20609294, 100990000000);


-- WRITE YOUR ANS HERE:

SELECT name, population, area FROM World
WHERE 
area >= 3000000
OR
population >= 25000000;
