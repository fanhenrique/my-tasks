import datetime as dt

class Node():

  def __init__(self, id:int, text:str, star:bool=False, date:float=None):
    self.id = id
    self.text = text
    self.star = star
    self.date = date if date else dt.datetime.now().timestamp()


  def change_star(self):
    self.star = not self.star
    return self.star


  def change_text(self, text:str):
    self.text = text
  