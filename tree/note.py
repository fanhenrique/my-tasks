import datetime as dt

import colored as colored

class Note():
  def __init__(self, id, text, star=False):
    self.id = id
    self.text = text
    self.star = star
    self.date = dt.datetime.now().timestamp()

  def __str__(self, level, date=False):
    return (
      colored.id(id=self.id, level=level) + 
      colored.note(text=self.text) + 
      (colored.date(date=self.date) if date else '') +
      (colored.star() if self.star else '')
    )


      
