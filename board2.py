import datetime as dt
import termcolor as tc

import colored
from task import Task
from note import Note

class Board2():
  def __init__(self, id, text, childrens=[], tasks=[], notes=[], check=False, started=False):
  # def __init__(self, id, text, childrens=[], check=False, started=False):
    self.id = id
    self.text = text
    self.childrens = childrens #subtasks path 
    self.tasks = tasks #list tasks
    self.notes = notes #list notes
    self.check = check
    self.started = started
    self.date = dt.datetime.now().timestamp()

  def __str__(self, level, info=None):
    return (
      colored.pipe(level=level) +
      colored.id(self.id) + 
      colored.board(self.text) +
      ('' if not info else ((colored.info(info[0], info[1]) if info else '') + colored.date(self.date)))
    )

  def count_tasks(self):
    return len(self.tasks)
  
  def count_notes(self):
    return len(self.notes)

  def count_tasks_checks(self):
    count_tasks_checks = 0
    for task in self.tasks:    
      if task.check:
        count_tasks_checks+=1
    return count_tasks_checks