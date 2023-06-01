import pathlib
import datetime as dt
from typing import Union
import termcolor as tc

import utils
import messagens.messagens as msg
from tree.board import Board
from tree.node import Node
from tree.note import Note
from tree.task import Task

priority_color = {0:'white', 1:'light_yellow', 2:'light_red'}
priority_attrs = {0:['bold'], 1:['bold'], 2:['bold', 'underline']}

pipe_icon = '\u2223'
star_icon = '\u2605'
check_icon = '\u2713'
started_icon = '\u25A3'
task_icon = '\u25A1'
note_icon = '\u25C9'

def pipe(color:str='dark_grey', attrs:list[str]=['dark', 'bold']):
  return tc.colored(
    text=f'{pipe_icon} ',
    color=color,
    attrs=attrs,
  )


def text(text:str, color:str='light_grey', attrs:list[str]=['dark', 'bold']):
  return tc.colored(
    text=text,
    color=color,
    attrs=attrs,
  )


def indentation(id:int, level:int):
  line = ''
  if level > 1:
    line += f'{pipe_icon}   '*(level-1)

  if level > 0:
    line += pipe_icon
    line += '  ' if id > 9 else '   '

  return tc.colored(text=f'{line}{id}.', color='dark_grey', attrs=['bold'])


def info(n1:int, n2:int):
  return tc.colored(
    text=f' [{n1}/{n2}]',
    color='dark_grey',
    attrs=['bold', 'dark'],
  )


def date(date:float):
  return tc.colored(
    text=f' {utils.count_date(date)}',
    color='dark_grey',
    attrs=['dark'],
  )


def star():  
  return tc.colored(
      text=f' {star_icon}',
      color='light_yellow',
    )


def board(text:str):
  return (
    tc.colored(
      text='@',
      color='green',
      attrs=['bold'],
    ) + 
    tc.colored(
      text=text,
      color='green',
      attrs=['bold','underline']
    )
  )


def task(text:str, check:bool=False, started:bool=False, priority:int=0):
  return (
    tc.colored(
      text=f'{check_icon} ' if check else f'{started_icon} ' if started else f'{task_icon} ',# '\u22EF ' '\u22C5'*2 '\u0387'*2 '\u2812 ',
      color='light_green' if check else 'blue' if started else priority_color[priority],
    ) +
    tc.colored(
      text=text,#''.join([f'\u0336{c}' for c in text]) if check else text,
      color='light_grey' if check else priority_color[priority],
      attrs=['dark'] if check else priority_attrs[priority],
    )
  )


def note(text:str):
  return (
    tc.colored(
      text=f'{note_icon} ',
      color='magenta',
    ) + 
    tc.colored(
      text=text,
      color='magenta',
    )
  )


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
  return (
    tc.colored(text=f'\n{complete:.2f}% ', color='white', attrs=['bold']) +
    text(text=f'of all tasks complete.\n') + 
    tc.colored(text=f'{check_icon} {done} ', color='light_green', attrs=['bold']) + text(text=f'done ') + pipe() +
    tc.colored(text=f'{pending} ', color='white', attrs=['bold']) + text(text='pending ') +
    tc.colored(text=f'{started_icon} {started} ', color='blue', attrs=['bold']) + text(text='started ') +
    tc.colored(text=f'{task_icon} {not_started_priority0} ', color=priority_color[0], attrs=['bold']) + 
    tc.colored(text=f'{task_icon} {not_started_priority1} ', color=priority_color[1], attrs=['bold']) +
    tc.colored(text=f'{task_icon} {not_started_priority2} ', color=priority_color[2], attrs=['bold']) +
    text(text=f'not started ') + pipe() +
    tc.colored(text=f'{note_icon} {notes} ',color='magenta', attrs=['bold']) + text(text='notes')
  )


def error():
  return tc.colored(text=msg.ERROR, color='light_red', attrs=['bold'])


def success():
  return tc.colored(text=msg.SUCCESS, color='green', attrs=['bold'])


def id(text:str, color:str='white', attrs:list[str]=['bold']):
  return tc.colored(text=text, color=color, attrs=attrs)


def confirmation_add(new:Node=None):
  if new:
    return success() + text(utils.string_type_node(new, first_upcase=True)) + ' ' + id(new.id) + text(' created')
  
def cannot_add_new_node(father:Union[Task, Note]=None):
  if father:
    if isinstance(father, Task):
      error_node = text(text='Cannot add a new node in a task')
    if isinstance(father, Note):
      error_node = text(text='Cannot add a new node in a note')
  
  return error() + error_node


def id_not_found(id_not_found:int):
  return(
    error() + 
    text('Node id ') + 
    id(str(id_not_found)) +
    text(' not found')
  )

def board_not_found_per_name(name:str):
   return(
    error() +
    text('Node with ') + 
    id(name) + 
    text(' name not found')
   ) 

def success_deleted(deleted:Node):
  return(
    success() + 
    text(utils.string_type_node(deleted, first_upcase=True)) + ' ' +
    id(deleted.id) + 
    text(' deleted')
  )


def priority_level_out_of_range():
  return f'{error()} {text(msg.PRIORITY_LEVEL_OUT_OF_RANGE)}'


def success_changed(node:Node):
  return f'{success()} {text(utils.string_type_node(node, first_upcase=True))} {id(node.id)}'


# changes in tasks
def success_changed_priority(node:Task):
  return f'{success_changed(node)} {text(msg.CHANGED_PRIORITY)}'

def success_changed_started(node:Task):
  return f'{success_changed(node)} {text(msg.STARTED)}'

def success_changed_not_started(node:Task):
  return f'{success_changed(node)} {text(msg.NOT_STARTED)}'

def success_changed_check(node:Task):
  return f'{success_changed(node)} {text(msg.CHECK)}'

def success_changed_not_check(node:Task):
  return f'{success_changed(node)} {text(msg.NOT_CHECK)}'


# change in nodes
def success_changed_star(node:Node):
  return f'{success_changed(node)} {text(msg.STAR)}'

def success_changed_not_star(node:Node):
  return f'{success_changed(node)} {text(msg.NOT_STAR)}'

def success_change_text(node:Node):
  return f'{success_changed(node)} {text(msg.EDITED)}'
    

# error only tasks
def error_only_tasks(node):
  message = text(f'{utils.string_type_node(node, first_upcase=True)} {id(node.id)}  {pipe()}')
  return f'{error()} {message}' 

def only_tasks_have_priority(node:Union[Note, Board]):
  return f'{error_only_tasks(node)} {text(msg.ONLY_TASKS_HAVE_PRIORITY)}'

def only_tasks_can_be_started(node:Union[Note, Board]):
  return f'{error_only_tasks(node)} {text(msg.ONLY_TASKS_CAN_BE_STARTED)}'

def only_tasks_can_be_checked(node:Union[Note, Board]):
  return f'{error_only_tasks(node)} {text(msg.ONLY_TASKS_CAN_BE_CHECKED)}'


# only used in timeline mode
def date_timeline(date:dt.datetime, n1:int, n2:int):
  message = text(
    f'{utils.WEEK[date.weekday()]} {utils.MONTHS[date.month]} {date.day} {date.year}',
    color='green',
    attrs=['bold', 'underline'])
  return f'{message} {info(n1, n2)}'
  

def invalid_id(invalid_id:int):
  return f'{error()} {text(msg.ID)} {id(invalid_id)} {text(msg.NOT_VALID)}'

# messagens about the tree 
def tree_empty():
  return f'{error()} {text(msg.TREE_EMPTY)}'

def new_tree_create(path_new_tree:pathlib.PosixPath):
  message = f'{msg.NEW_TREE_CREATE_IN} {str(path_new_tree)}'
  return f'{success()} {text(message)}'

def first_node_must_be_a_board():
  return f'{error()} {text(msg.THE_FIRST_NODE_MUST_BE_A_BOARD)}'
