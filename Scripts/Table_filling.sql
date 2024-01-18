

INSERT INTO tag (tag_name) VALUES 
-- Add following info:
('Whatever tag1 you want'),
('Whatever tag2 you want');



INSERT INTO person (person_name) VALUES 
('Whatever name1 you want'),
('Whatever name2 you want ');


INSERT INTO task (
	task_name, 
	start_date, 
	end_date,
	person_id,
	task_status)
	VALUES
	-- Add following info:
	('task name', 'start date', 'due date', 'personal_id', 'done'),
	('task name', 'start date', 'due date', 'personal_id', ''); 


INSERT INTO task_tag (
task_id, tag_id)
VALUES
-- Add following info:
(1, 1),
(1, 2);






