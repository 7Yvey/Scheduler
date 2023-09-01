'''todo '''

#Imported modules
import sqlite3
from todo_database_access import DatabaseAccess
from todo_classes import Person, Task, Tag, TaskTag


database = "/home/Yvey/Documents/SQL/TODO/todo.db"
con = sqlite3.connect(database)
access = DatabaseAccess(con)

#Instruction

done = False
while not done:
    print("""Choose a following number to do what you want:    
        1. View all tasks 
        2. View a specific tasks
        3. Edit task
        4. Delete task
        5. Create new task
        6. Add person
        7. Add tag
    """)
    selection = int(input())


    ## 1. View all tasks     
    if selection == 1:
        
        res = access.read_all_tasks()
        for task in res:
            all_tags = []
            print(task)
            for tag in task.tags:
                all_tags.append(tag.tag_name)
            print(f"tags = {all_tags}")

    ## 2. View a specific tasks
    if selection == 2:
        ## Insert task id 
        print("Insert task id")
        id = int(input())
        res = access.read_task(task_id = id)
        all_tags = []
        print(res)
        for tag in res.tags:
            all_tags.append(tag.tag_name)
        print(f"tags = {all_tags}")

    ## 3. Edit task
    if selection == 3:
        print("Insert task id of the task you want to edit:")
        id = int(input())
        print("Insert task name:")
        task_name = input()
        print("Insert start date in formate YYYY-MM-DD")
        start_date = input()
        print("Insert due date in formate YYYY-MM-DD")
        end_date = input()
        print("Has the task already been done? y/n")
        status_question = input()

        if status_question == 'Y' or status_question == 'y':
            task_status = 'done'
        
        if status_question == 'N' or status_question == 'n':
            task_status = ''



        ## Choose person        
        print("Choose one person from following list for task and use person id")
        view_people = access.read_people()
        for person in view_people:
            print(person.person_id, person.person_name)
        
        print("Insert person id")
        person_id = int(input())
        person = access.read_person(person_id)
        
        ## Choose tag
        print(f"""Choose tag from following list after its tags id: 
         """)
        view_all_tags = access.read_all_tags()
        for item in view_all_tags:
            print(item.tag_id, item.tag_name)

        enough_tags = False
        tags = []
        while not enough_tags:
            tag_id = int(input())
            tag = access.read_tag(tag_id)
            tags.append(tag)

            print("Do you want to add more tags? y/n")
            response = input()    
            if response == 'n' or response == 'N':
                print("All tags were added")
                enough_tags = True

        task = Task(task_id = id, task_name = task_name, 
        start_date = start_date, end_date = end_date, tags = tags,
        person = person, task_status = task_status)

        update = access.update_task(task = task)

    ## 4. Delete task
    if selection == 4:
        print("Insert task id you want to delete")

        all_tasks = access.read_all_tasks()
        all_task_ids = []    
        for task in all_tasks:
            all_task_ids.append(task.task_id)
        
        task_id = int(input())
        if task_id in all_task_ids:
            to_delete = access.delete_task(task_id = task_id)
            
        else:
            print("""Selected task is not in database. 
            Please choose id of existing task""")

        

    ## 5. Create new task
    if selection == 5:
        print("Insert task name:")
        task_name = input()
        print("Insert start date in formate YYYY-MM-DD")
        start_date = input()
        print("Insert due date in formate YYYY-MM-DD")
        end_date = input()
        print("Has the task already been done? y/n")
        status_question = input()

        if status_question == 'Y' or status_question == 'y':
            task_status = 'done'
        
        if status_question == 'N' or status_question == 'n':
            task_status = ''

        ## Choose person        
        print("Choose one person from following list for task and use person id")
        view_people = access.read_people()
        for person in view_people:
            print(person.person_id, person.person_name)
        
        print("Insert person id")
        person_id = int(input())
        person = access.read_person(person_id)
        
        ## Choose tag
        print(f"""Choose tag from following list after its tags id: 
        """)
        view_all_tags = access.read_all_tags()
        for item in view_all_tags:
            print(item.tag_id, item.tag_name)

        enough_tags = False
        tags = []
        while not enough_tags:
            tag_id = int(input())
            tag = access.read_tag(tag_id)
            tags.append(tag)

            print("Do you want to add more tags? y/n")
            response = input()    
            if response == 'n' or response == 'N':
                print("All tags were added")
                enough_tags = True

        task = Task(task_name = task_name, 
        start_date = start_date, end_date = end_date, tags = tags,
        person = person, task_status = task_status)

        added_tags = []
        for tag in task.tags:
            added_tags.append(tag.tag_id, tag.tag_name)
        print(f"""This is created task. 
        {task}, tags = {added_tags}
        Do you want to save into the database? y/n """)
        save_task = input()

        if save_task == 'y' or save_task == 'Y':
            add_new_task = access.insert_task(task = task)
            print("The task was saved into database")

    ## 6. Add person to the database
    if selection == 6:
        print("These are people already prresent in database")
        view_people = access.read_people()
        for person in view_people:
            print(person.person_id, person.person_name)

        print("""For addition of new person into the database,
        please write name of a new person""")
        person_name = input()

        new_person = Person(person_name = person_name)
        add_person = access.insert_person(person = new_person)


    ## 7. Add tag
    if selection == 7:
        print("These are tags already present in database")
        view_tags = access.read_tag()
        for tag in view_tags:
            print(tag.tag_id, tag.tag_name)

        print("""For addition of new tag into the database,
        please write name of a new tag""")
        tag_name = input()

        new_tag = Tag(tag_name = tag_name)
        add_tag = access.insert_tag(tag = new_tag)


    print(f" Are you done? Y/N")
    end = input()
    if end == "Y" or  end == "y":
        done = True
    
