import datetime as dt
import termcolor as tc

from colored import colored_id

priority_color = {0:'light_grey', 1:'light_yellow', 2:'light_red'}
priority_attrs = {0:[], 1:['bold'], 2:['bold', 'underline', 'blink']}

class Task():
  def __init__(self, id, text, check=False, started=False, star=False, priority=0):
    self.id = id
    self.text = text
    self.check = check
    self.started = started
    self.star = star
    self.priority = priority
    self.date = dt.datetime.now().timestamp()
  

  def __str__(self):
    return colored_id(self.id) + tc.colored(
        text='\u2714 ' if self.check else'\u25A1 ',
        color='light_green' if self.check else priority_color[self.priority],
        attrs=[],
        ) + tc.colored(
          self.text,
          color=priority_color[self.priority],
          attrs=priority_attrs[self.priority],
        )
      