'''todo database connected to python'''

import sqlite3
from typing import List, Tuple, Dict

class Person:
    '''Description of a person'''

    def __init__(self, person_name: str, person_id: int = None):
        self.person_id = person_id
        self.person_name = person_name
    
class Tag:
    '''Description of tag'''

    def  __init__(self, tag_name: str, tag_id: int = None):
        self.tag_id = tag_id
        self.tag_name = tag_name

    def __str__(self):
            return f"""
            tag_id = {self.tag_id}, 
            tag_name = {self.tag_name}""" 

class Task:
    '''Description of task'''

    def __init__(self, task_name: str, start_date: str,
     end_date:str, person: Person, 
     task_status: str, tags: List[Tag], task_id: int = None):
        self.task_id = task_id
        self.task_name = task_name
        self.start_date = start_date
        self.end_date = end_date
        self.person_id = person.person_id
        self.task_status = task_status
        self.tags = tags

    def __str__(self):
        return f"""
        task_id = {self.task_id}, 
        task_name = {self.task_name}, 
        start_date = {self.start_date},
        end_date = {self.end_date},
        person_id = {self.person_id},
        task_status = {self.task_status}""" 

class TaskTag:
    '''Description of task and tags'''

    def __init__(self,task_id: int, tag_id: int, task_name: Task, tag_name: Tag):
        self.task_id = task_id
        self.tag_id = tag_id
        self.task_name = task_name
        self.tag_name = tag_name

    def create_dict(self):
        param_dict = {}
        param_dict['task_id'] = self.task_id
        param_dict['tag_id'] = self.tag_id
       # param_dict['task_name'] = self.task_name
       # param_dict['tag_name'] = self.tag_name
        return param_dict