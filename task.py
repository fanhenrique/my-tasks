import datetime as dt
import termcolor as tc

import colored

class Task():
  def __init__(self, id, text, check=False, started=False, star=False, priority=0):
    self.id = id
    self.text = text
    self.check = check
    self.started = started
    self.star = star
    self.priority = priority
    self.date = dt.datetime.now().timestamp()
  

  def __str__(self, level, date=False):
    return (
      colored.id(id=self.id, level=level) + 
      colored.task(text=self.text, check=self.check, started=self.started, priority=self.priority) +
      (colored.date(date=self.date) if date else '') + 
      colored.star(star=self.star)
    )
      