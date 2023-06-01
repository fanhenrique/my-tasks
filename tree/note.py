import messages.messages as msg
from .node import Node

class Note(Node):

  def __str__(self, level:int=0, show_date:bool=False):
    return super().__str__(
      core=msg.note(text=self.text),
      level=level,
      show_date=show_date
    )
