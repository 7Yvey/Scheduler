DELETE FROM tag; 

INSERT INTO tag (tag_name) VALUES 
('work'),
('personal growth'),
('relax'),
('fun'),
('social events'),
('house work'),
('cultural events'),
('clothes shopping'),
('self care'),
('shopping');

DELETE FROM person;

INSERT INTO person (person_name) VALUES 
('Matous'),
('Iveta');


DELETE FROM tag;
SELECT * FROM tag;


INSERT INTO task (
	task_name, 
	start_date, 
	end_date,
	person_id)
	VALUES
	('going to the cinema', '2023-08-05', '2023-08-06', 1),
	('cleaning up the library', '2023-08-05', '2023-08-06', 2),
	('cleaning up croscs', '2023-08-05', '2023-08-05', 2),
	('cleaning the floor', '2023-08-05', '2023-08-06', 1),
	('washing up the windows', '2023-08-05', '2023-12-23', 1),
	('sort the wardrobe', '2023-08-12', '2023-08-31', 2),
	('improve wardrobe', '2023-08-14', '2023-09-30', 2),
	('have a meeting with Jirina', '2023-08-08', '2023-08-14', 2),
	('write some part of article about Corenybacterium', '2023-08-04', '2023-08-08', 2),
	('visit festival Hrady', '2023-08-12', '2023-08-13', 1),
	('visit festival Hrady', '2023-08-12', '2023-08-13', 2);
	

INSERT INTO task_tag (
task_id, tag_id)
VALUES
(1, 3),
(1, 4),
(1, 5),
(1, 7),
(2, 2),
(2, 6),
(3, 1),
(3, 2),
(4, 1),
(4, 2),
(5, 6),
(6, 3),
(6, 4),
(7, 6),
(8, 6),
(9, 2),
(9, 6),
(9, 9),
(10, 2),
(10, 9),
(10, 10),	
(11, 2),
(12, 1),
(12, 2),
(13, 1),
(13, 2),
(14, 1),
(15, 1),
(15, 2);





