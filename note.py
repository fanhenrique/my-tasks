import datetime as dt
import termcolor as tc

import colored

class Note():
  def __init__(self, id, text, star=False):
    self.id = id
    self.text = text
    self.star = star
    self.date = dt.datetime.now().timestamp()

  def __str__(self, level):
    return (
      colored.pipe(level=level) +
      colored.id(id=self.id) + 
      colored.note(text=self.text) + 
      colored.date(date=self.date) +
      colored.star(star=self.star)
    )


      
