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
      text=' \u2605' if star else '',
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

priority_color = {0:'white', 1:'light_yellow', 2:'light_red'}
priority_attrs = {0:['bold'], 1:['bold'], 2:['bold', 'underline']}

def task(text, check=False, started=False, priority=0):
  return (
    tc.colored(
      text='\u2713 ' if check else '\u25A3 ' if started else '\u25A1 ',# '\u22EF ' '\u22C5'*2 '\u0387'*2 '\u2812 ',
      color='light_green' if check else 'blue' if started else priority_color[priority],
      attrs= []
    ) + #tc.colored(text='aa', color='dark_grey', attrs=[]) +
    tc.colored(
      text=text,#''.join([f'\u0336{c}' for c in text]) if check else text,
      color='light_grey' if check else priority_color[priority],
      attrs=['dark'] if check else priority_attrs[priority],
    )
  )

def note(text):
  return (
    tc.colored(
      text='\u25C9 ',#'\u25C8 '
      color='magenta',
      attrs=[],
    ) + 
    tc.colored(
      text=text,
      color='magenta',
      attrs=[],
    )
  )

def all_tree_info(complete, done, pending, started, not_started, notes):

  line1 = f'\n{complete:.2f}% of all tasks complete.\n'
  d = f'{done} '
  p = f'{pending} '
  s = f'{started} '
  ns = f'{not_started} '
  n = f'{notes} '

  return (
    tc.colored(
      text=line1,
      color='light_grey',
      attrs=['dark'],
    ) + 
    tc.colored(
      text='\u2713 '+d,
      color='light_green',
      attrs=['bold'],
    ) + tc.colored(text='done \u2223 ', color='light_grey', attrs=['dark', 'bold']) +
    tc.colored(
      text=p,
      color='white',
      attrs=['bold'],
    ) + tc.colored(text='pending ', color='light_grey', attrs=['dark', 'bold']) +
    tc.colored(
      text='\u25A3 '+s,
      color='blue',
      attrs=['bold'],
    ) + tc.colored(text='started ', color='light_grey', attrs=['dark', 'bold']) +
    tc.colored(
      text='\u25A1 ',
      color=priority_color[0],
      attrs=[],
    ) +
    tc.colored(
      text='\u25A1 ',
      color=priority_color[1],
      attrs=[],
    ) +
    tc.colored(
      text='\u25A1 ',
      color=priority_color[2],
      attrs=[],
    ) +
    tc.colored(
      text=ns,
      color='white',
      attrs=['bold'],
    ) + tc.colored(text='not started \u2223 ', color='light_grey', attrs=['dark', 'bold']) +
    tc.colored(
      text='\u25C9 '+n,
      color='magenta',
      attrs=['bold'],
    ) + tc.colored(text='notes', color='light_grey', attrs=['dark', 'bold'])


  )
