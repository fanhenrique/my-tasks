import termcolor as tc

import utils

def id(id, level):
  l = ''
  if level > 1:
    l+='\u2223  '*(level-1)

  if level > 0:
    l+='\u2223'
    l += ' ' if id > 9 else '  '

  
  return (
    tc.colored(
      text=l,#'|  '*level,
      color='dark_grey',
      attrs=['bold'],
    ) +
    tc.colored(
      text=repr(id)+'.',
      color='dark_grey',
      attrs=['bold'],
    )
  )

def info(n1, n2):
  return tc.colored(
    text=' ['+n1+'/'+n2+']',
    color='dark_grey',
    attrs=['bold', 'dark'],
  )

def date(date):
  return tc.colored(
    text=' '+utils.count_date(date),
    color='dark_grey',
    attrs=['dark'],
  )

def star(star=False):
  return tc.colored(
      text=' \u2B50' if star else '',
      color='light_yellow',
    )

def board(text):
  return (
    tc.colored(
      text='#',
      color='light_green',
      attrs=['bold'],
    ) + 
    tc.colored(
      text=text,
      color='light_green',
      attrs=['bold','underline']
    )
  )

priority_color = {0:'light_grey', 1:'light_yellow', 2:'light_red'}
priority_attrs = {0:[], 1:['bold'], 2:['bold', 'underline', 'blink']}

def task(text, check=False, started=False, priority=0):
  return (
    tc.colored(
      text='\u2714 ' if check else '\u2026 ' if started else '\u25A1 ',
      color='light_green' if check else priority_color[priority],
      attrs=[],
    ) + 
    tc.colored(
      text=text,
      color=priority_color[priority],
      attrs=priority_attrs[priority],
    )
  )

def note(text):
  return (
    tc.colored(
      text='\u25CF ',
      color='light_blue',
      attrs=[],
    ) + 
    tc.colored(
      text=text,
      color='light_grey',
      attrs=[],
    )
  )