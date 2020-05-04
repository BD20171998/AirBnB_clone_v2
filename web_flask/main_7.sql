-- Drop all rows in states and insert new
USE hbnb_dev_db;

DELETE FROM `cities`;
DELETE FROM `states`;

INSERT INTO `states` (id, created_at, updated_at, name) VALUES 
    ('f2ab504a-503d-4216-b4e3-d6ee676d0f16','2016-03-25 19:42:40','2016-03-25 19:42:40','aczmclkril'),
    ('d2ab504a-503d-4216-b4e3-d6ee676d0f16','2016-03-25 19:42:40','2016-03-25 19:42:40','vczmclkril');

INSERT INTO `cities` (id, state_id, created_at, updated_at, name) VALUES 
    ('f6a92db1-1a67-4975-8381-ea95731fad6b', 'f2ab504a-503d-4216-b4e3-d6ee676d0f16','2016-03-25 19:42:40','2016-03-25 19:42:40','dzjmnmihny'), 
    ('8478c2d5-d9cf-4893-a381-a6307914a11f', 'f2ab504a-503d-4216-b4e3-d6ee676d0f16','2016-03-25 19:42:40','2016-03-25 19:42:40','khpiaeezfs'), 
    ('a4e63494-4232-4e09-bc9d-09720d767704', 'f2ab504a-503d-4216-b4e3-d6ee676d0f16','2016-03-25 19:42:40','2016-03-25 19:42:40','mroevsntnd'), 
    ('959faf21-c328-46b1-a04d-7e117093396b', 'd2ab504a-503d-4216-b4e3-d6ee676d0f16','2016-03-25 19:42:40','2016-03-25 19:42:40','ahwhznewde'), 
    ('33903e35-c164-4c76-a004-9e3c1586bbe4', 'd2ab504a-503d-4216-b4e3-d6ee676d0f16','2016-03-25 19:42:40','2016-03-25 19:42:40','txyzbwdqqu');
