import sqlite3
from todo_database_access import DatabaseAccess
from todo_classes import Person, Task, Tag, TaskTag
from BasicScreens import Screen, EndScreen 
from PeopleScreens import PeopleScreen, ShowPersonScreen, InitialScreen, AddPersonScreen, DelPersonScreen

database = "/home/Yvey/Documents/SQL/TODO/todo.db"
con = sqlite3.connect(database)
access = DatabaseAccess(con)
 

current_screen = InitialScreen(access)
while current_screen.is_not_last_screen():
    current_screen.show_selection()
    user_input = input()
    print(f"You have chosen {user_input}")
    current_screen = current_screen.get_next_screen(user_input)
print("ended")

