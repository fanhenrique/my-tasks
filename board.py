import datetime as dt
import termcolor as tc

from colored import colored_id
from task import Task
from note import Note

class Board():
  # def __init__(self, id, text, childrens=[], tasks=[], notes=[], check=False, started=False):
  def __init__(self, id, text, childrens=[], check=False, started=False):
    self.id = id
    self.text = text
    self.childrens = childrens #subtasks path 
    # self.tasks = tasks #list tasks
    # self.notes = notes #list notes
    self.check = check
    self.started = started
    self.date = dt.datetime.now().timestamp()

  def __str__(self):
    return colored_id(self.id) + tc.colored(
      text='#',
      color='light_green',
      attrs=['bold'],
    ) + tc.colored(
      text=self.text+' ['+self.count_tasks_checks()+']',
      color='light_green',
      attrs=['bold','underline']
    )
     
  def count_tasks(self):
    count_tasks = 0
    for child in self.childrens:
      if isinstance(child, Task):
        count_tasks+=1
    return count_tasks
  
  def count_notes(self):
    count_notes = 0
    for child in self.childrens:
      if isinstance(child, Note):
        count_notes+=1
    return count_notes

  def count_tasks_checks(self):
    count_tasks_checks = 0
    for child in self.childrens:
      if isinstance(child, Task):
        if child.check:
          count_tasks_checks+=1
    return str(count_tasks_checks)