import datetime as dt

import messages.messages as msg

class Node():

  def __init__(self, id:int, text:str, star:bool=False, date:float=None):
    self.id = id
    self.text = text
    self.star = star
    self.date = date if date else dt.datetime.now().timestamp()

  def __str__(self, core:str, level:int=0, show_date:bool=False):
    return (
      msg.indentation(id=self.id, level=level) + 
      core + 
      (msg.date(date=self.date) if show_date else '') +
      (msg.star() if self.star else '')
    )


  def change_star(self):
    self.star = not self.star
    return self.star


  def change_text(self, text:str):
    self.text = text
  