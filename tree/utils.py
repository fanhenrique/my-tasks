import datetime as dt

from .note import Note
from .task import Task
from .board import Board

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


def type_node(node):
  if isinstance(node, Note):
    return 'Note'
  elif isinstance(node, Task):
    return 'Task'
  elif isinstance(node, Board):
    return 'Board'