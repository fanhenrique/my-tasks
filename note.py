import datetime as dt
import termcolor as tc

from colored import colored_id
class Note():
  def __init__(self, id, text, star=False):
    self.id = id
    self.text = text
    self.star = star
    self.date = dt.datetime.now().timestamp()

  def __str__(self):
    return colored_id(self.id) + tc.colored(
        text='\u25CF ',
        color='light_blue',
        attrs=[],
      ) + tc.colored(
        text=self.text,
        color='light_grey',
        attrs=[],
      )