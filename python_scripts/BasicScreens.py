
#Imported modules
import sqlite3
from todo_database_access import DatabaseAccess
# from todo_classes import Person, Task, Tag, TaskTag


class Screen:
    '''Represents basic screen'''
    def __init__(self, access: DatabaseAccess):
        self.access = access

    def show_selection(self):
        '''A selection what to do/ where to move'''
        print( "To go back to previous screen press 'b' ")
        print("To go back to home screen press 'h'")
        print("To quit press 'q'")

    def get_next_screen(self):
        '''A way to move to another screen'''
        pass

    def is_not_last_screen(self):
        '''ending the program'''
        return True


class InitialScreen(Screen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        '''A selection what to do/ where to move'''
        print("Welcome to manage your 'TODO'. Select from following: ")
        print( """
        1. Manage tasks 
        2. Manage people""")
        
        print("To quit press 'q'")

    def get_next_screen(self, user_input: int):
        '''A way to move to another screen''' 
        if user_input == 'q':
            return EndScreen(self)

        elif user_input == '1':
            from TaskScreen import TaskScreen
            return TaskScreen(self.access)
        
        elif user_input == '2':
            from PeopleScreens import PeopleScreen
            return PeopleScreen(self.access)




class EndScreen(Screen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def is_not_last_screen(self):
        return False


