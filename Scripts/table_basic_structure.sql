DROP TABLE tag;

CREATE TABLE tag (
	tag_id INTEGER PRIMARY KEY,
	tag_name TEXT NOT NULL,
);

DROP TABLE person;

CREATE TABLE person (
	person_id INTEGER PRIMARY KEY,
	person_name TEXT NOT NULL,
);


DROP TABLE task;

CREATE TABLE task(
	task_id INTEGER PRIMARY KEY,
	task_name TEXT NOT NULL,
	start_date TEXT,
	end_date TEXT ,
	person_id INTEGER NOT NULL,
	FOREIGN KEY (person_id) REFERENCES person (person_id)
);

DROP TABLE task_tag;

CREATE TABLE task_tag (
	task_id INTEGER NOT NULL,
	tag_id INTEGER NOT NULL,
	PRIMARY KEY (task_id, tag_id)
	FOREIGN KEY (task_id) REFERENCES task (task_id),
	FOREIGN KEY (tag_id) REFERENCES tag (tag_id)
);