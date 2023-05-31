import colored
from .node import Node

class Note(Node):

  def __str__(self, level:int=0 , show_date:bool=False):
    return (
      colored.indentation(id=self.id, level=level) + 
      colored.note(text=self.text) + 
      (colored.date(date=self.date) if show_date else '') +
      (colored.star() if self.star else '')
    )
