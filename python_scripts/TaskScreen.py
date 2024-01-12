
#Imported modules
import sqlite3
from todo_database_access import DatabaseAccess
from todo_classes import Person, Task, Tag, TaskTag
from BasicScreens import Screen, EndScreen, InitialScreen

class TaskScreen(Screen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)
     
    def show_selection(self):
        print("1. View all tasks ")
        print("2. Filter tasks")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Create new task")
        Screen.show_selection(self)
 
    def get_next_screen(self, user_input):
        if user_input == 'q':
            return EndScreen(self.access)

        elif user_input == '1':
            return AllTasksScreen(self.access)

        elif user_input == '2':
            from FilterTaskScreen import FilterTasksScreen
            return FilterTasksScreen(self.access)

        elif user_input == '3':
            return EditTaskScreen(self.access)
        
        elif user_input == '4':
            return DeleteTaskScreen(self.access)
        
        elif user_input == '5':
            return NewTaskScreen(self.access)

        elif user_input == 'h':
            return InitialScreen(self.access)

        elif user_input == 'b':
            return InitialScreen(self.access)
        
        else:
            print("Unknow option")
            return self


class AllTasksScreen(Screen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        res = self.access.read_all_tasks()
        for task in res:
            all_tags = []
            print(task)
            for tag in task.tags:
                all_tags.append(tag.tag_name)
            print(f"tags = {all_tags}")
            
        Screen.show_selection(self)


    def get_next_screen(self,user_input):
        if user_input == 'q':
            return EndScreen(self.access)

        elif user_input == 'h':
            return InitialScreen(self.access)

        elif user_input == 'b':
            return TaskScreen(self.access)

        else:
            print("Unknow option")
            return self


class EditTaskScreen(AllTasksScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)
    
    def show_selection(self):
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
        view_people = self.access.read_people()
        for person in view_people:
            print(person.person_id, person.person_name)
        
        print("Insert person id")
        person_id = int(input())
        person = self.access.read_person(person_id)
        
        ## Choose tag
        print(f"""Choose tag from following list after its tags id: 
         """)
        view_all_tags = self.access.read_all_tags()
        for item in view_all_tags:
            print(item.tag_id, item.tag_name)

        enough_tags = False
        tags = []
        while not enough_tags:
            tag_id = int(input())
            tag = self.access.read_tag(tag_id)
            tags.append(tag)

            print("Do you want to add more tags? y/n")
            response = input()    
            if response == 'n' or response == 'N':
                print("All tags were added")
                enough_tags = True

        task = Task(task_id = id, task_name = task_name, 
        start_date = start_date, end_date = end_date, tags = tags,
        person = person, task_status = task_status)

        update = self.access.update_task(task = task)
        
        ## End of Edit task shows where to move next
        Screen.show_selection(self)
        

class DeleteTaskScreen(AllTasksScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        print("Insert task id you want to delete")
        all_tasks = self.access.read_all_tasks()
        all_task_ids = []    
        for task in all_tasks:
            all_task_ids.append(task.task_id)
        
        task_id = int(input())
        if task_id in all_task_ids:
            to_delete = self.access.delete_task(task_id = task_id)
            
        else:
            print("""Selected task is not in database. 
            Please choose id of existing task""")
    
        ## Endo of Delete task shows where to move
        Screen.show_selection(self)
   

class NewTaskScreen(AllTasksScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
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
        view_people = self.access.read_people()
        for person in view_people:
            print(person.person_id, person.person_name)
        
        print("Insert person id")
        person_id = int(input())
        person = self.access.read_person(person_id)
        
        ## Choose tag
        print(f"""Choose tag from following list after its tags id: 
        """)
        view_all_tags = self.access.read_all_tags()
        for item in view_all_tags:
            print(item.tag_id, item.tag_name)

        enough_tags = False
        tags = []
        while not enough_tags:
            tag_id = int(input())
            tag = self.access.read_tag(tag_id)
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
            added_tags.append([tag.tag_id, tag.tag_name])
        print(f"""This is created task. 
        {task}, tags = {added_tags}
        Do you want to save into the database? y/n """)
        save_task = input()

        if save_task == 'y' or save_task == 'Y':
            add_new_task = self.access.insert_task(task = task)
            print("The task was saved into database")
    
        ## End of Adding of a new task, shows where to move next
        Screen.show_selection(self)