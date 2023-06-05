import datetime as dt

from tree.note import Note
from tree.task import Task
from tree.board import Board

HEADER_CSV = ('node', 'id', 'date', 'star', 'text', 'children', 'check', 'started', 'priority')


def string_type_node(node, first_upcase=False):
  if isinstance(node, Note):
    return 'Note' if first_upcase else 'note'
  elif isinstance(node, Task):
    return 'Task' if first_upcase else 'task'
  elif isinstance(node, Board):
    return 'Board' if first_upcase else 'board'


def all_args_are_empty(args):
  for arg in args:
    if args[arg]:
      return False
  return True
    
