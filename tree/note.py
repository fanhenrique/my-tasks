import messagens.colored as colored
from .node import Node

class Note(Node):

  def __str__(self, level:int=0, show_date:bool=False):
    return super().__str__(
      core=colored.note(text=self.text),
      level=level,
      show_date=show_date
    )
