import pathlib
import datetime as dt
from typing import Union
import termcolor as tc

import utils
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
  return tc.colored(text='ERROR ', color='light_red', attrs=['bold'])


def success():
  return tc.colored(text='SUCCESS ', color='green', attrs=['bold'])


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


def success_changed(node:Node):
  return(
    success() +
    text(utils.string_type_node(node, first_upcase=True)) + ' ' +
    id(node.id)
  )

# changes in tasks 
def success_changed_priority(node:Task):
  return success_changed(node) + text(' changed priority')

def success_changed_started(node:Task):
  return success_changed(node) + text(' started')

def success_changed_not_started(node:Task):
  return success_changed(node) + text(' not started')

def success_changed_check(node:Task):
  return success_changed(node) + text(' check')

def success_changed_not_check(node:Task):
  return success_changed(node) + text(' not check')

# change in nodes
def success_changed_star(node:Node):
  return success_changed(node) + text(' star')

def success_changed_not_star(node:Node):
  return success_changed(node) + text(' not star')

def success_change_text(node:Node):
  return success_changed(node) +  text(' edited')


def priority_level_out_of_range():
  return(
    error() +
    text('Priority level out of range')
  )


# error only tasks
def error_only_tasks(node):
  return error() + text(utils.string_type_node(node, first_upcase=True)) + ' ' + id(node.id) + ' ' + pipe()

def only_tasks_have_priority(node:Union[Note, Board]):
  return error_only_tasks(node) + text('Only tasks have priority')

def only_tasks_can_be_started(node:Union[Note, Board]):
  return error_only_tasks(node)  + text('Only tasks can be started')

def only_tasks_can_be_checked(node:Union[Note, Board]):
  return error_only_tasks(node) + text('Only tasks can be checked')


# only used in timeline mode
def date_timeline(date:dt.datetime, n1:int, n2:int):
  return (
    text(f'{utils.WEEK[date.weekday()]} {utils.MONTHS[date.month]} {date.day} {date.year}', color='green', attrs=['bold', 'underline']) +  
    info(n1, n2)
  )


def invalid_id(invalid_id:int):
  return error() + text('id ') + id(invalid_id) + text(' not valid')


def tree_empty():
  return error() + text('Tree is empty')


def first_node_must_be_a_board():
  return error() + text('The first node must be a board')


def new_tree_create(path_new_tree:pathlib.PosixPath):
  return success() + text(f'NEW TREE CREATE in {str(path_new_tree)}')