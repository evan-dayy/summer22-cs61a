.read data.sql


CREATE TABLE bluedog AS
  SELECT color, 
         pet
  FROM students
  WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
    SELECT color, 
           pet,
           song
  FROM students
  WHERE color = 'blue' AND pet = 'dog';;


CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM students 
  group by smallest
  having count(1) = 1;


CREATE TABLE matchmaker AS
  SELECT t1.pet,
         t1.song,
         t1.color,
         t2.color

  from students t1, students t2
  where t1.pet = t2.pet and t1.song = t2.song and t1.time < t2.time;

