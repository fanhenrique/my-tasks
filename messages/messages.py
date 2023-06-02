import pathlib
import datetime as dt
from typing import Union
import termcolor as tc

import utils
import messages.colored as c
import messages.texts as txt
import messages.colored as colored
from tree.board import Board
from tree.node import Node
from tree.note import Note
from tree.task import Task


def pipe():
  return tc.colored(f'{txt.PIPE_ICON}', color=c.PIPE_COLOR, attrs=c.PIPE_ATTRS)


def text(text:str):
  return tc.colored(text, color=c.TEXT_COLOR, attrs=c.TEXT_ATTRS)


def indentation(id:int, level:int):
  line = ''
  if level > 1:
    line += f'{txt.PIPE_ICON}   '*(level-1)

  if level > 0:
    line += txt.PIPE_ICON
    line += '  ' if id > 9 else '   '

  return tc.colored(text=f'{line}{id}.', color=c.INDENTATION_COLOR, attrs=c.INDENTATION_ATTRS)


def info(n1:int, n2:int):
  return tc.colored(f'[{n1}/{n2}]', color=c.INFO_COLOR, attrs=c.INFO_ATTRS)


def date(date:float):
  return tc.colored(text=f'{utils.count_date(date)}', color=c.DATE_COLOR, attrs=c.DATE_ATTRS)


def star():  
  return tc.colored(f'{txt.STAR_ICON}', color=c.STAR_COLOR)


def board(text:str):
  colored_icon = tc.colored(f'{txt.BOARD_ICON}', color=c.BOARD_ICON_COLOR, attrs=c.BOARD_ICON_ATTRS)
  colored_text = tc.colored(text, color=c.BOARD_TEXT_COLOR, attrs=c.BOARD_TEXT_ATTRS)
  return f'{colored_icon}{colored_text}'


def task(text:str, check:bool, started:bool, priority:int):

  icon = txt.CHECK_ICON if check else txt.STARTED_ICON if started else txt.TASK_ICON
  icon_color = c.CHECK_ICON_COLOR if check else c.STARTED_ICON_COLOR if started else c.PRIORITY_ICON_COLOR[priority]
  colored_icon = tc.colored(icon, color=icon_color)

  text_color = c.CHECK_TEXT_COLOR if check else c.PRIORITY_TEXT_COLOR[priority]
  text_attrs = c.CHECK_TEXT_ATTRS if check else c.PRIORITY_TEXT_ATTRS[priority]
  colored_text = tc.colored(text, color=text_color, attrs=text_attrs)

  return f'{colored_icon} {colored_text}'


def note(text:str):
  return tc.colored(f'{txt.NOTE_ICON} {text}', color=c.NOTE_COLOR)

def all_tree_info(
    complete:float,
    done:int,
    pending:int,
    started:int,
    not_started_priority0:int,
    not_started_priority1:int,
    not_started_priority2:int,
    notes:int
  ):

  txt_complete = tc.colored(f'\n{complete:.2f}%', color=c.COMPLETE_COLOR, attrs=c.COMPLETE_ATTRS)
  of_all_tasks_complete = text(f'{txt.OF_ALL_TASKS_COMPLETE}')
  i = f'{txt_complete} {of_all_tasks_complete}'

  check_icon = tc.colored(f'{txt.CHECK_ICON} {done}', color=c.CHECK_ICON_COLOR, attrs=c.CHECK_ICON_ATTRS)
  txt_done = text(f'{txt.DONE}')
  d = f'{check_icon} {txt_done}'

  num_pending = tc.colored(f'{pending}', color=c.PENDING_NUM_COLOR, attrs=c.PENDING_NUM_ATTRS)
  txt_pending = text(f'{txt.PENDING}')
  p = f'{num_pending} {txt_pending}' 

  started_icon  = tc.colored(f'{txt.STARTED_ICON} {started}', color=c.STARTED_ICON_COLOR, attrs=c.STARTED_ICON_ATTRS)
  txt_started = text(f'{txt.STARTED}')
  s = f'{started_icon} {txt_started}'

  priority0_icon = tc.colored(f'{txt.TASK_ICON} {not_started_priority0}', color=c.PRIORITY_ICON_COLOR[0], attrs=c.PRIORITY_ICON_ATTRS[0])
  priority1_icon = tc.colored(f'{txt.TASK_ICON} {not_started_priority1}', color=c.PRIORITY_ICON_COLOR[1], attrs=c.PRIORITY_ICON_ATTRS[1])
  priority2_icon = tc.colored(f'{txt.TASK_ICON} {not_started_priority2}', color=c.PRIORITY_ICON_COLOR[2], attrs=c.PRIORITY_ICON_ATTRS[2])

  txt_not_started = text(f'{txt.NOT_STARTED}')
  ns = f'{priority0_icon} {priority1_icon} {priority2_icon} {txt_not_started}'
  
  note_icon = tc.colored(f'{txt.NOTE_ICON} {notes}', color=c.NOTE_COLOR)
  txt_notes = text(f'{txt.NOTES}')
  n = f'{note_icon} {txt_notes}'

  return f'{i} {d} {pipe()} {p} {s} {ns} {pipe()} {n}'

def error():
  return tc.colored(txt.ERROR, color=c.ERROR_COLOR, attrs=c.ERROR_ATTRS)

def success():
  return tc.colored(txt.SUCCESS, color=c.SUCCESS_COLOR, attrs=c.SUCCESS_ATTRS)


def id(id:str):
  return tc.colored(id, color=c.ID_COLOR, attrs=c.ID_ATTRS)


def confirmation_add(new:Node=None):
  if new:
    return f'{success()} {text(utils.string_type_node(new, first_upcase=True))} {id(new.id)} {text(txt.CREATED)}'
  
def cannot_add_new_node(father:Union[Task, Note]=None):
  if father:
    if isinstance(father, Task):
      error_node = text(text=txt.CANNOT_ADD_A_NEW_NODE_IN_A_TASK)
    if isinstance(father, Note):
      error_node = text(text=txt.CANNOT_ADD_A_NEW_NODE_IN_A_NOTE)
  
  return f'{error()} {error_node}'


def id_not_found(id_not_found:int):
  return f'{error()} {text(txt.NODE_ID)} {id(str(id_not_found))} {text(txt.NOT_FOUND)}'
  

def board_not_found_per_name(name:str):
   return f'{error()} {text(txt.NODE_WITH)} {id(name)} {text(txt.NAME_NOT_FOUND)}'


def success_deleted(deleted:Node):
  message = f'{text(utils.string_type_node(deleted, first_upcase=True))}'
  return f'{success()} {message} {id(deleted.id)} {text(txt.DELETED)}'


def priority_level_out_of_range():
  return f'{error()} {text(txt.PRIORITY_LEVEL_OUT_OF_RANGE)}'


def success_changed(node:Node):
  return f'{success()} {text(utils.string_type_node(node, first_upcase=True))} {id(node.id)}'


# changes in tasks
def success_changed_priority(node:Task):
  return f'{success_changed(node)} {text(txt.CHANGED_PRIORITY)}'

def success_changed_started(node:Task):
  return f'{success_changed(node)} {text(txt.STARTED)}'

def success_changed_not_started(node:Task):
  return f'{success_changed(node)} {text(txt.NOT_STARTED)}'

def success_changed_check(node:Task):
  return f'{success_changed(node)} {text(txt.CHECK)}'

def success_changed_not_check(node:Task):
  return f'{success_changed(node)} {text(txt.NOT_CHECK)}'


# change in nodes
def success_changed_star(node:Node):
  return f'{success_changed(node)} {text(txt.STAR)}'

def success_changed_not_star(node:Node):
  return f'{success_changed(node)} {text(txt.NOT_STAR)}'

def success_change_text(node:Node):
  return f'{success_changed(node)} {text(txt.EDITED)}'
    

# error only tasks
def error_only_tasks(node):
  message = text(f'{utils.string_type_node(node, first_upcase=True)} {id(node.id)}  {pipe()}')
  return f'{error()} {message}' 

def only_tasks_have_priority(node:Union[Note, Board]):
  return f'{error_only_tasks(node)} {text(txt.ONLY_TASKS_HAVE_PRIORITY)}'

def only_tasks_can_be_started(node:Union[Note, Board]):
  return f'{error_only_tasks(node)} {text(txt.ONLY_TASKS_CAN_BE_STARTED)}'

def only_tasks_can_be_checked(node:Union[Note, Board]):
  return f'{error_only_tasks(node)} {text(txt.ONLY_TASKS_CAN_BE_CHECKED)}'


# only used in timeline mode
def date_timeline(date:dt.datetime, n1:int, n2:int):
  message = text(
    f'{utils.WEEK[date.weekday()]} {utils.MONTHS[date.month]} {date.day} {date.year}',
    color=c.DATE_TIMELINE_COLOR,
    attrs=c.DATE_TIMELINE_ATTRS)
  return f'{message} {info(n1, n2)}'
  

def invalid_id(invalid_id:str):
  return f'{error()} {text(txt.ID)} {id(invalid_id)} {text(txt.INVALID)}'

# messagens about the tree 
def tree_empty():
  return f'{error()} {text(txt.TREE_EMPTY)}'

def new_tree_create(path_new_tree:pathlib.PosixPath):
  message = f'{txt.NEW_TREE_CREATE_IN} {str(path_new_tree)}'
  return f'{success()} {text(message)}'

def first_node_must_be_a_board():
  return f'{error()} {text(txt.THE_FIRST_NODE_MUST_BE_A_BOARD)}'
