import datetime as dt

import colored as colored

class Note():

  def __init__(self, id:int, text:str, star:bool=False, date:float=None):
    self.id = id
    self.text = text
    self.star = star
    self.date = date if date else dt.datetime.now().timestamp()


  def __str__(self, level:int=0 , date:bool=False):
    return (
      colored.indentation(id=self.id, level=level) + 
      colored.note(text=self.text) + 
      (colored.date(date=self.date) if date else '') +
      (colored.star() if self.star else '')
    )


  def change_star(self):
    self.star = not self.star
    return self.star


  def change_text(self, text:str):
    self.text = text
    

      
