
#Imported modules
import sqlite3
from todo_database_access import DatabaseAccess
from todo_classes import Person, Task, Tag, TaskTag
from BasicScreens import Screen, EndScreen, InitialScreen


class PeopleScreen(Screen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)
    
    def show_selection(self):
        '''A selection what to do/ where to move'''
        print( """
        1. Show people
        2. Add person 
        3. Delete person
        """)
        Screen.show_selection(self)

    def get_next_screen(self, user_input: int):
        '''A way to move to another screen'''
        if user_input == 'q':
            return EndScreen

        elif user_input == '1':
            return ShowPersonScreen(self.access)

        elif user_input == '2':
            return AddPersonScreen(self.access)
        
        elif user_input == '3':
            return DelPersonScreen(self.access)

        elif user_input == 'h':
            return InitialScreen(self.access)

        elif user_input == 'b':
            return InitialScreen(self.access)


        
        else:
            print("Unknow option")
            return self



class ShowPersonScreen(Screen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        print("These are people already present in database")
        view_people = self.access.read_people()
        for person in view_people:
            print(person.person_id, person.person_name)

        Screen.show_selection(self)

    def get_next_screen(self, user_input: int):
        if user_input == 'q':
            return EndScreen(self.access)

        elif user_input == 'b':
            return PeopleScreen(self.access)

        elif user_input == 'h':
            return InitialScreen(self.access)

        else:
            print("Unknow option")
            return self



class AddPersonScreen(ShowPersonScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        '''A selection what to do/ where to move'''
        print("These are people already present in database")
        view_people = self.access.read_people()
        for person in view_people:
            print(person.person_id, person.person_name)

        print("""For addition of new person into the database,
        please write name of a new person""")
        person_name = input()

        new_person = Person(person_name = person_name)
        add_person = self.access.insert_person(person = new_person)

        Screen.show_selection(self)


class DelPersonScreen(ShowPersonScreen):
    def __init__(self, access: DatabaseAccess):
        super().__init__(access)

    def show_selection(self):
        print("Choose one person from following list for task and use person id")
        view_people = self.access.read_people()
        for person in view_people:
            print(person.person_id, person.person_name)
        
        print("Insert person id")
        person_id = int(input())
        person = self.access.read_person(person_id)
        print(person.person_name, person.person_id)
        deleted_person = self.access.delete_person(person)

        Screen.show_selection(self)
        