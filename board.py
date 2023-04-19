import datetime as dt
import termcolor as tc

import colored
from task import Task
from note import Note

class Board():

  def __init__(self, id, text, childrens=[], check=False, star=False):
    self.id = id
    self.text = text
    self.childrens = childrens #subtasks path or tasks or notes
    self.check = check
    self.star = star
    self.date = dt.datetime.now().timestamp()

  def __str__(self, level, info=None, date=False):
    return (
      colored.pipe(level)+
      colored.id(self.id) + 
      colored.board(self.text) +
      (colored.info(info[0], info[1]) if info else '') +
      (colored.date(self.date) if date else '') +
      colored.star(star=self.star)
    )

  def count_tasks(self):
    ct = 0
    for child in self.childrens:
      if isinstance(child, Task):
        ct+=1
    return ct
  
  def count_notes(self):
    nt = 0
    for child in self.childrens:
      if isinstance(child, Note):
        nt+=1
    return nt

  def count_tasks_checks(self):
    ct = 0
    for child in self.childrens:
      if isinstance(child, Task):
        if child.check: 
          ct+=1
    return ct
