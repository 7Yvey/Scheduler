
#Imported modules
import sqlite3
from todo_database_access import DatabaseAccess
from todo_classes import Person, Task, Tag, TaskTag
from BasicScreens import Screen, EndScreen, InitialScreen



class FilterTasksScreen(Screen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        print("1. Filter tasks using task ID")
        print("2. Filter tasks using person ID")
        print("3. Filter done tasks")
        print("4. Filter NOT done tasks")
        print("5. Filter tasks using due date")
        Screen.show_selection(self)
    
    def get_next_screen(self, user_input):
        if user_input == 'q':
            return EndScreen(self.access)
        
        elif user_input == '1':
            return FiltTasksIDScreen(self.access)

        elif user_input == '2':
            return FiltPersonTaskScreen(self.access)

        elif user_input == '3':
            return DoneTasksScreen(self.access)

        elif user_input == '4':
            return NotDoneTasksScreen(self.access)

        elif user_input == '5':
            return DueDateTaskScreen(self.access)
        
        elif user_input == 'b':
            from TaskScreen import TaskScreen
            return TaskScreen(self.access)
        
        elif user_input == 'h':    
            return InitialScreen(self.access)

        else:
            print("Unknow option")
            return self
        

class FiltTasksIDScreen(Screen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)


    def show_selection(self):
        print("Insert task id")
        id = int(input())
        res = self.access.read_task(task_id = id)
        all_tags = []
        print(res)
        for tag in res.tags:
            all_tags.append(tag.tag_name)
        print(f"tags = {all_tags}")

        Screen.show_selection(self)


    def get_next_screen(self, user_input):
        if user_input == 'q':
            return EndScreen(self.access)

        elif user_input == 'b':
            return FilterTasksScreen(self.access)

        elif user_input == 'h':
            return InitialScreen(self.access)

        else:
            print("Unknow option")
            return self


class FiltPersonTaskScreen(FiltTasksIDScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

##To DO
    def show_selection(self):
        print(f"Insert person id")
        person_id = int(input())
        res = self.access.show_person_tasks(person_id = person_id)

        for task in res:
            all_tags = []
            print(task)
            for tag in task.tags:
                all_tags.append(tag.tag_name)
            print(f"tags = {all_tags}")

        Screen.show_selection(self)


class DoneTasksScreen(FiltTasksIDScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        self.access.show_done_task()
        Screen.show_selection(self.access)


class NotDoneTasksScreen(FiltTasksIDScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        self.access.show_not_done_task()
        Screen.show_selection(self.access)


class DueDateTaskScreen(FiltTasksIDScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)
##To DO
    def show_selection(self):

        print("Neni hotove :D")
        Screen.show_selection(self.access)
