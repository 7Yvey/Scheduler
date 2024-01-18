

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
('shopping')
;


INSERT INTO person (person_name) VALUES 
('Matous'),
('Iveta');


INSERT INTO task (
	task_name, 
	start_date, 
	end_date,
	person_id,
	task_status)
	VALUES 

	('going to the cinema', '2024-01-13', '2024-02-28', 1, ''),
	('cleaning up the library', '2024-01-05', '2024-02-06', 2, ''),
	('cleaning up the kitechen cabinets', '2024-01-05', '2024-02-05', 2, ''),
	('cleaning the floor', '2024-01-20', '2024-01-25', 1, ''),
	('cleaning up the bathhroom', '2024-01-13', '2024-01-23', 1, ''),
	('sort the wardrobe', '2024-02-01', '2024-02-10', 2, ''),
	('have a meeting with Jirina', '2024-01-25', '2024-01-25', 2, ''),
	('Find dream job in IT', '2024-01-01', '2024-02-28', 2, ''),
	('read and correct arcticle about Corenybacterium', '2024-01-30', '2024-01-31', 2, ''),
	('get dress for Cosples Brno', '2024-01-12', '2024-02-23', 2, ''),
	('get costume for Cosples Brno', '2024-01-12', '2024-02-23', 1, ''),
	('party at Cosples Brno', '2024-02-24', '2024-02-24', 1, ''),
	('party at Cosples Brno', '2024-02-24', '2023-02-24', 2, '');




INSERT INTO task_tag (
task_id, tag_id)
VALUES
(1, 3),
(1, 4),
(1, 5),
(1, 7),
(2, 6),
(2, 9),
(3, 6),
(3, 9),
(4, 6),
(5, 6),
(6, 6),
(6, 9),
(7, 1),
(8, 1),
(9, 1),
(10, 8),
(10, 10),
(11, 8),
(11, 10),
(12, 4),
(12, 5),
(12, 7),
(13, 4),
(13, 5),
(13, 7);





