import datetime as dt

import colored as colored

from .node import Node

allowed_priorities = [0,1,2]

class Task(Node):
  
  def __init__(self, id:int, text:str, check:bool=False, started:bool=False, star:bool=False, priority:int=0, date:float=None):
    super().__init__(id, text, star, date)
    self.check = check
    self.started = started
    if priority not in allowed_priorities:
      raise IndexError
    self.priority = priority 
    
  
  def __str__(self, level:int=0, show_date:bool=False):
    return (
      colored.indentation(id=self.id, level=level) + 
      colored.task(text=self.text, check=self.check, started=self.started, priority=self.priority) +
      (colored.date(date=self.date) if show_date else '') + 
      (colored.star() if self.star else '')
    )
  

  def change_check(self):
    self.check = not self.check
    return self.check


  def change_started(self):
    self.started = not self.started
    return self.started


  def change_priority(self, priority:int):

    if priority not in allowed_priorities:
      raise IndexError

    self.priority = allowed_priorities[priority]
