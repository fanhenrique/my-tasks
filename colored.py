
import termcolor as tc

from tree.note import Note
from tree.task import Task

import utils

priority_color = {0:'white', 1:'light_yellow', 2:'light_red'}
priority_attrs = {0:['bold'], 1:['bold'], 2:['bold', 'underline']}

pipe_icon = '\u2223'
star_icon = '\u2605'
check_icon = '\u2713'
started_icon = '\u25A3'
task_icon = '\u25A1'
note_icon = '\u25C9'

def pipe(color='dark_grey', attrs=['dark', 'bold']):
  return tc.colored(
    text=f'{pipe_icon} ',
    color=color,
    attrs=attrs,
  )


def text(text, color='light_grey', attrs=['dark', 'bold']):
  return tc.colored(
    text=text,
    color=color,
    attrs=attrs,
  )


def indentation(id, level):
  line = ''
  if level > 1:
    line += f'{pipe_icon}  '*(level-1)

  if level > 0:
    line += pipe_icon
    line += ' ' if id > 9 else '  '

  return tc.colored(text=f'{line}{id}.', color='dark_grey', attrs=['bold'])


def info(n1, n2):
  return tc.colored(
    text=f' [{n1}/{n2}]',
    color='dark_grey',
    attrs=['bold', 'dark'],
  )


def date(date):
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


def board(text):
  return (
    tc.colored(
      text='#',
      color='green',
      attrs=['bold'],
    ) + 
    tc.colored(
      text=text,
      color='green',
      attrs=['bold','underline']
    )
  )


def task(text, check=False, started=False, priority=0):
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


def note(text):
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


def all_tree_info(complete, done, pending, started, not_started, notes):

  return (
    tc.colored(text=f'\n{complete:.2f}% ', color='white', attrs=['bold']) +
    text(text=f'of all tasks complete.\n') + 
    tc.colored(text=f'{check_icon} {done} ', color='light_green', attrs=['bold']) + text(text=f'done ') + pipe() +
    tc.colored(text=f'{pending} ', color='white', attrs=['bold']) + text(text='pending ') +
    tc.colored(text=f'{started_icon} {started} ', color='blue', attrs=['bold']) + text(text='started ') +
    tc.colored(text=f'{task_icon} ', color=priority_color[0]) + 
    tc.colored(text=f'{task_icon} ', color=priority_color[1]) +
    tc.colored(text=f'{task_icon} ', color=priority_color[2]) +
    tc.colored(text=f'{not_started} ', color='white', attrs=['bold']) + text(text=f'not started ') + pipe() +
    tc.colored(text=f'{note_icon} {notes} ',color='magenta', attrs=['bold']) + text(text='notes')
  )


def error():
  return tc.colored(text='ERROR ', color='light_red', attrs=['bold'])


def success():
  return tc.colored(text='SUCCESS ', color='green', attrs=['bold'])


def id(text, color='white', attrs=['bold']):
  return tc.colored(text=text, color=color, attrs=attrs)


def confirmation_add(confirmation, father=None, new=None):
  
  if confirmation:
    return success() + text(utils.string_type_node(new, first_upcase=True)) + ' ' + id(new.id) + text(' created')
  else:
    if father:
      if isinstance(father, Task):
        error_node = text(text='Cannot add a new node in a task')
      if isinstance(father, Note):
        error_node = text(text='Cannot add a new node in a note')
    
    return error() + error_node


def id_not_found(id_not_found):
  return(
    error() + 
    text('Node id ') + 
    id(str(id_not_found)) +
    text(' not found')
  )


def success_deleted(deleted):
  return(
    success() + 
    text(utils.string_type_node(deleted, first_upcase=True)) + ' ' +
    id(deleted.id) + 
    text(' deleted')
  )


def success_changed(changed, text_changed):
  return(
    success() +
    text(utils.string_type_node(changed, first_upcase=True)) + ' ' +
    id(changed.id) + ' ' +
    text(text_changed)
  )


def success_change_text(node):
  return success() + text(utils.string_type_node(node, first_upcase=True)) + ' ' + id(node.id) +  text(' edited')

def priority_level_out_of_range():
  return(
    error() +
    text('Priority level out of range')
  )


def only_tasks_have_priority(node):
  return error() + text(utils.string_type_node(node, first_upcase=True)) + ' ' + id(node.id) + ' ' + pipe() + text('Only tasks have priority')


def only_tasks_can_be_started(node):
  return error() + text(utils.string_type_node(node, first_upcase=True)) + ' ' + id(node.id) + ' ' + pipe() + text('Only tasks can be started')


def only_tasks_can_be_checked(node):
  return error() + text(utils.string_type_node(node, first_upcase=True)) + ' ' + id(node.id) + ' ' + pipe() + text('Only tasks can be checked')
