import datetime as dt

import colored as colored

allowed_priorities = [0,1,2]

class Task():
  
  def __init__(self, id, text, check=False, started=False, star=False, priority=0, date=None):
    self.id = id
    self.text = text
    self.check = check
    self.started = started
    self.star = star
    if priority not in allowed_priorities:
      raise IndexError
    self.priority = priority 
    self.date = date if date else dt.datetime.now().timestamp()
  

  def __str__(self, level=0, date=False):
    return (
      colored.indentation(id=self.id, level=level) + 
      colored.task(text=self.text, check=self.check, started=self.started, priority=self.priority) +
      (colored.date(date=self.date) if date else '') + 
      (colored.star() if self.star else '')
    )
  

  def change_text(self, text):
    self.text = text


  def change_check(self):
    self.check = not self.check
    return self.check


  def change_started(self):
    self.started = not self.started
    return self.started


  def change_star(self):
    self.star = not self.star
    return self.star


  def change_priority(self, priority):

    if priority not in allowed_priorities:
      raise IndexError

    self.priority = allowed_priorities[priority]
