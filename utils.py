import datetime as dt

from tree.note import Note
from tree.task import Task
from tree.board import Board

def count_date(date):
    diference = dt.datetime.now().timestamp() - date
    
    if diference < 60:
      return 'now'
    elif diference >= 60 and diference < 3600:
      time = int(diference/60)
      return str(time)+'min'
    elif diference >= 3600 and diference < 86400:
      time = int(diference/3600)
      return str(time)+'h'
    elif diference >= 86400 and diference < 604800:
      time = int(diference/86400)
      return str(time)+'d'
    elif diference >= 604800 and diference < 31536000:
      time = int(diference/604800)
      return str(time)+'week'
    elif diference >= 31536000:
      time = int(diference/31536000)
      return str(time)+'year'

def string_type_node(node, first_upcase=False):
  if isinstance(node, Note):
    return 'Note' if first_upcase else 'note'
  elif isinstance(node, Task):
    return 'Task' if first_upcase else 'note'
  elif isinstance(node, Board):
    return 'Board' if first_upcase else 'note'


def find_missing(x):
  x.sort()
  difference = list(set(range(x[0], x[-1]+1)).difference(x))
  
  return difference[0] if len(difference) else x[-1]+1
  

