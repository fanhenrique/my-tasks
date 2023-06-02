import pathlib
import datetime as dt
from typing import Union

import utils
import messages.texts as txt
import messages.colored as colored
from tree.board import Board
from tree.node import Node
from tree.note import Note
from tree.task import Task

PRIORITY_COLOR = {0:'white', 1:'light_yellow', 2:'light_red'}
PRIORITY_ATTRS = {0:['bold'], 1:['bold'], 2:['bold', 'underline']}

CHECK_ICON_COLOR = 'light_green'
STARTED_ICON_COLOR = 'blue'

CHECK_TEXT_COLOR = 'light_grey'
CHECK_TEXT_ATTRS = ['dark']


def pipe():
  return colored.dark_grey_dark_bold(text=f'{txt.PIPE_ICON}')


def text(text:str):
  return colored.light_grey_dark_bold(text=text)


def indentation(id:int, level:int):
  line = ''
  if level > 1:
    line += f'{txt.PIPE_ICON}   '*(level-1)

  if level > 0:
    line += txt.PIPE_ICON
    line += '  ' if id > 9 else '   '

  return colored.dark_grey_bold(text=f'{line}{id}.')


def info(n1:int, n2:int):
  return colored.dark_grey_dark_bold(text=f' [{n1}/{n2}]')


def date(date:float):
  return colored.dark_grey_dark(text=f' {utils.count_date(date)}')


def star():  
  return colored.light_yellow(f' {txt.STAR_ICON}')


def board(text:str):
  colored_icon = colored.green_bold(f'{txt.BOARD_ICON}')
  colored_text = colored.green_bold_underline(text=text)
  return f'{colored_icon}{colored_text}'


#''.join([f'\u0336{c}' for c in text]) if check else text,
def task(text:str, check:bool=False, started:bool=False, priority:int=0):

  icon = txt.CHECK_ICON if check else txt.STARTED_ICON if started else txt.TASK_ICON
  icon_color = CHECK_ICON_COLOR if check else STARTED_ICON_COLOR if started else PRIORITY_COLOR[priority]
  colored_icon = colored.colored(text=icon, color=icon_color)

  text_color = CHECK_TEXT_COLOR if check else PRIORITY_COLOR[priority]
  text_attrs = CHECK_TEXT_ATTRS if check else PRIORITY_ATTRS[priority]
  colored_text = colored.colored(text=text, color=text_color, attrs=text_attrs)

  return f'{colored_icon} {colored_text}'


def note(text:str):
  return colored.magenta(text=f'{txt.NOTE_ICON} {text}')

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

  txt_complete = colored.white_bold(f'\n{complete:.2f}%')
  of_all_tasks_complete = text(f'{txt.OF_ALL_TASKS_COMPLETE}')
  i = f'{txt_complete} {of_all_tasks_complete}'

  check_icon = colored.light_green_bold(f'{txt.CHECK_ICON} {done}')
  txt_done = text(f'{txt.DONE}')
  d = f'{check_icon} {txt_done}'

  num_pending = colored.white_bold(f'{pending}')
  txt_pending = text(f'{txt.PENDING}')
  p = f'{num_pending} {txt_pending}' 

  started_icon  = colored.blue_bold(f'{txt.STARTED_ICON} {started}')
  txt_started = text(f'{txt.STARTED}')
  s = f'{started_icon} {txt_started}'

  priority0_icon = colored.colored(f'{txt.TASK_ICON} {not_started_priority0}', color=PRIORITY_COLOR[0], attrs=PRIORITY_ATTRS[0])
  priority1_icon = colored.colored(f'{txt.TASK_ICON} {not_started_priority1}', color=PRIORITY_COLOR[1], attrs=PRIORITY_ATTRS[1])
  priority2_icon = colored.light_red_bold(f'{txt.TASK_ICON} {not_started_priority2}')

  txt_not_started = text(f'{txt.NOT_STARTED}')
  ns = f'{priority0_icon} {priority1_icon} {priority2_icon} {txt_not_started}'
  
  note_icon = colored.magenta_bold(f'{txt.NOTE_ICON} {notes}')
  txt_notes = text(f'{txt.NOTES}')
  n = f'{note_icon} {txt_notes}'

  return f'{i} {d} {pipe()} {p} {s} {ns} {pipe()} {n}'

def error():
  return colored.light_red_bold(text=txt.ERROR)

def success():
  return colored.green_bold(text=txt.SUCCESS)


def id(id:str):
  return colored.white_bold(text=id)


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
    color='green',
    attrs=['bold', 'underline'])
  return f'{message} {info(n1, n2)}'
  

def invalid_id(invalid_id:int):
  return f'{error()} {text(txt.ID)} {id(invalid_id)} {text(txt.NOT_VALID)}'

# messagens about the tree 
def tree_empty():
  return f'{error()} {text(txt.TREE_EMPTY)}'

def new_tree_create(path_new_tree:pathlib.PosixPath):
  message = f'{txt.NEW_TREE_CREATE_IN} {str(path_new_tree)}'
  return f'{success()} {text(message)}'

def first_node_must_be_a_board():
  return f'{error()} {text(txt.THE_FIRST_NODE_MUST_BE_A_BOARD)}'
