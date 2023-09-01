
import sqlite3
from typing import List, Tuple, Dict
from todo_classes import Person, Task, Tag, TaskTag


class DatabaseAccess:

    def __init__(self, sql_connect:sqlite3.Connection):
        self.sql_connect = sql_connect

    #### Person
    def insert_person(self, person: Person) -> Person:
        '''Inserts new person into database'''
        param_dict = {
            'person_name': person.person_name
        }
        cur = self.sql_connect.cursor()
        cur.execute("INSERT INTO person VALUES(NULL, :person_name)", param_dict)
        self.sql_connect.commit()
        id = cur.lastrowid
        cur.close()

        return Person(person_id = id, person_name = person.name)

    def read_person(self, id: int) -> Person:
        '''Reads specific name and id of a specific person'''
        cur = self.sql_connect.cursor()
        cur.execute("SELECT * FROM person WHERE person_id = ? ", (id, ))
        res = cur.fetchone()
        person = Person(person_name = res[1], person_id = res[0])
        cur.close()
        return person

    def read_people(self) -> List[Person]:
        '''Reads information about all people in the database'''
        cur = self.sql_connect.cursor()
        cur.execute("SELECT * FROM person")
        res = cur.fetchall()
        people = []
        for i in res:
            person = Person(person_name = i[1], person_id = i[0])
            people.append(person)
        cur.close()
        return people


    def update_person(self, person: Person) -> Person:
        '''Updates information about specific person depending on person_id'''
        cur = self.sql_connect.cursor()
        cur.execute("UPDATE person SET person_name = ? WHERE person_id = ?", (person.person_name, person.person_id,))
        self.sql_connect.commit()
        cur.close()
        return person
        

    def delete_person(self, person: Person):
        '''Deletes specific person from the database'''
        cur = self.sql_connect.cursor()
        cur.execute("DELETE FROM person WHERE person_id = ?", (person.person_id, ))
        self.sql_connect.commit()
        cur.close()


    ####### TAGS

    def insert_tag(self, tag: Tag) -> Tag:
        '''Inserts new tag into database'''
        param_dict = {
            'tag_id': tag.tag_id,
            'tag_name': tag.tag_name
        }
        cur = self.sql_connect.cursor()
        cur.execute("INSERT INTO tag VALUES(:tag_id, :tag_name)", param_dict)
        self.sql_connect.commit()
        id = cur.lastrowid
        cur.close()

        return Tag(tag_id = id, tag_name = tag.tag_name)

    def read_tag(self, tag_id: int) -> Tag:
        '''Reads specific tag depending on its tag_id'''
        cur = self.sql_connect.cursor()
        cur.execute("SELECT * FROM tag WHERE tag_id = ? ", (tag_id, ))
        res = cur.fetchone()
        tag = Tag(tag_name = res[1], tag_id = res[0])
        cur.close()
        return tag

    def read_all_tags(self) -> List[Tag]:
        '''Reads all tags in database'''
        cur = self.sql_connect.cursor()
        cur.execute("SELECT * FROM tag")
        res = cur.fetchall()
        tags = []
        for i in res:
            tag = Tag(tag_name = i[1], tag_id = i[0])
            tags.append(tag)
        cur.close()
        return tags

    def update_tag(self, tag: Tag) -> Tag:
        '''Updates tag'''
        cur = self.sql_connect.cursor()
        cur.execute("UPDATE tag SET tag_name = ? WHERE tag_id = ?", (tag.tag_name, tag.tag_id,))
        self.sql_connect.commit()
        cur.close()
        return tag
        

    def delete_tag(self, tag: Tag):
        '''Deletes tag from database'''
        cur = self.sql_connect.cursor()
        cur.execute("DELETE FROM tag WHERE tag_id = ?", (tag.tag_id, ))
        self.sql_connect.commit()
        cur.close()


    ### Tasks
    def insert_task(self, task: Task) -> Task:
        '''Inserts task into database'''
        
        param_dict = {
            'task_id': task.task_id,
            'task_name': task.task_name,
            'start_date': task.start_date,
            'end_date': task.end_date,
            'person_id': task.person_id,
            'task_status': task.task_status
        }
        cur = self.sql_connect.cursor()
        cur.execute("""INSERT INTO task 
        VALUES 
        (:task_id, :task_name, :start_date, :end_date, :person_id, :task_status)""", param_dict)
        self.sql_connect.commit()
        task_id = cur.lastrowid
        print(task_id)
        
        cur.execute("""SELECT
            t.task_id,
            p.person_name,
            p.person_id
        FROM
            task AS t 
        JOIN person AS p ON t.person_id = p.person_id
        WHERE t.task_id = ? """, (task_id, ))
        res = cur.fetchone()
        print(res)
        person = Person(person_name = res[1], person_id = res[2])

        tags = task.tags
        task_tag_input = []
        for tag in tags:
            tag_tupl = (task_id, tag.tag_id)
            task_tag_input.append(tag_tupl)        

        cur.executemany("""INSERT INTO task_tag
        VALUES (?, ?) """, task_tag_input)
        self.sql_connect.commit()
        
        cur.close()

        return Task(
            task_id = id, 
            task_name =task.task_name, 
            start_date = task.start_date, 
            end_date = task.end_date, 
            person = person, 
            task_status = task.task_status,
            tags = tags 
        )

    def read_task(self, task_id: int) -> Task:
        '''Reads specific task depending on its task_id'''
        cur = self.sql_connect.cursor()
        cur.execute(""" SELECT 
            t.task_id,
            t.task_name,
            t.start_date,
            t.end_date,
            p.person_name,
            p.person_id,
            t.task_status,
            ta.tag_id, 
            ta.tag_name
        FROM
            task AS t 
        LEFT JOIN task_tag AS tt ON t.task_id = tt.task_id 
        LEFT JOIN tag AS ta ON ta.tag_id = tt.tag_id 
        LEFT JOIN person AS p ON t.person_id = p.person_id
        WHERE t.task_id = ? """, (task_id, ) )
        res_tags = cur.fetchall()
        all_tags = []
        for tag in res_tags:
            all_tags.append(Tag(tag_id = tag[7], tag_name = tag[8]))
        res_task = res_tags[0]
        task_person = Person(person_id = res_task[4], person_name = res_task[5])
        task = Task(
            task_id = res_task[0], 
            task_name = res_task[1], 
            start_date = res_task[2], 
            end_date = res_task[3], 
            person = task_person, 
            task_status = res_task[6],
            tags = all_tags  
        )

        cur.close()
        return task

    def read_all_tasks(self)  -> List[Task]:
        '''Reads all task in the database'''
        cur = self.sql_connect.cursor()
        cur.execute("""  SELECT 
            t.task_id,
            t.task_name,
            t.start_date,
            t.end_date,
            p.person_id,
            p.person_name,
            t.task_status,
            ta.tag_id, 
            ta.tag_name
        FROM
            task AS t 
        LEFT JOIN task_tag AS tt ON t.task_id = tt.task_id 
        LEFT JOIN tag AS ta ON ta.tag_id = tt.tag_id 
        LEFT JOIN person AS p ON t.person_id = p.person_id
        --WHERE t.task_id > 21 AND t.task_id < 24
        GROUP BY t.task_id, ta.tag_id, ta.tag_name""")
        res = cur.fetchall()
        finished_tasks = []
        unfinished_task = None
        unifinished_tags = []
        current_task = None
        current_id = None
        previous_id = None
        for item in res:
            current_id = item[0]        

            if previous_id != current_id and unfinished_task != None:    
                current_task.tags += unifinished_tags
                finished_tasks.append(unfinished_task)

            if current_id == previous_id:
                not_first_tag = Tag(tag_id = item[7], tag_name = item[8])
                unifinished_tags.append(not_first_tag)               

            else:
                person = Person(person_id = item[4], person_name = item[5])
                fist_tag = [Tag(tag_id = item[7], tag_name = item[8])]
                
                current_task = Task(
                    task_id = item[0], 
                    task_name = item[1], 
                    start_date = item[2], 
                    end_date = item[3], 
                    person = person, 
                    task_status = item[6],
                    tags = fist_tag
                )
                unfinished_task = current_task
                unifinished_tags = []
                previous_id = current_id

        current_task.tags += unifinished_tags
        finished_tasks.append(unfinished_task)

        cur.close()
        return finished_tasks
            

    def update_task(self, task: Task) -> Task:
        '''Updates specific task in the database'''
        cur = self.sql_connect.cursor()
        param_dict = {
            'task_id': task.task_id,
            'task_name': task.task_name,
            'start_date': task.start_date,
            'end_date': task.end_date,
            'person': task.person_id,
            'task_status': task.task_status
        }

        cur.execute("""UPDATE task SET task_name =:task_name, 
        start_date = :start_date, end_date = :end_date, person_id = :person,
        task_status = :task_status
        WHERE task_id = :task_id """, param_dict)
        self.sql_connect.commit()

        cur.execute("""SELECT tag_id FROM task_tag WHERE task_id = :task_id""", param_dict )
        old_tags = cur.fetchall()
        new_tags = []
        tags = task.tags
        task_id = (param_dict['task_id'],)
        for tag in tags:
            new_tags.append((tag.tag_id, ))
        
        ### to update
        diff_new_old = list(set(new_tags) - set(old_tags))
        to_update = []
        for new_item in diff_new_old:
            to_update.append(task_id + new_item)
        cur.executemany("""INSERT INTO task_tag VALUES (?, ?)""", to_update)
        self.sql_connect.commit()

        ## to delete alternative
        diff_old_new = list(set(old_tags) - set(new_tags))
        for item in diff_old_new:
            to_delete = task_id + item
            cur.execute("""DELETE FROM task_tag WHERE task_id = ? AND tag_id = ?""", to_delete)
            self.sql_connect.commit()
            to_delete = None

        cur.close()
        return task
    

    def delete_task(self, task_id: int):
        '''delete task '''
        delete_task_id = (task_id, )
        cur = self.sql_connect.cursor()
        cur.execute("DELETE FROM task WHERE task_id = ?", delete_task_id)
        cur.execute("DELETE FROM task_tag WHERE task_id = ?", delete_task_id)
        self.sql_connect.commit() 
        cur.close()


    def mark_done(self, task_id: int):
        '''Marks tasks as done'''
        cur = self.sql_connect.cursor()
        cur.execute("UPDATE task SET task_status = 'done' WHERE task_id = ?" , task_id)
        self.sql_connect.commit()

    def show_done_task(self):
        '''Shows done tasks'''
        cur = self.sql_connect.cursor()
        cur.execute("SELECT * FROM task WHERE task_status = 'done' ")
        print(cur.fetchall())


    def show_urgent_tasks(sql_cursor: sqlite3.Cursor):
        '''Shows task with the closest due date'''
        pass








