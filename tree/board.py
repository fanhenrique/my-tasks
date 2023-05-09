import datetime as dt

from collections import deque

import colored as colored

from .task import Task
from .note import Note


class Board():

  def __init__(self, id, text, children=deque(), star=False, date=None):
    self.id = id
    self.text = text
    self.children = children #subtasks path or tasks or notes
    self.star = star
    self.date = date if date else dt.datetime.now().timestamp()

  def __str__(self, level, info=None, date=False):
    return (      
      colored.indentation(id=self.id, level=level) + 
      colored.board(self.text) +
      (colored.info(info[0], info[1]) if info else '') +
      (colored.date(self.date) if date else '') +
      (colored.star() if self.star else '')
    )

  def change_text(self, text):
    self.text = text

  def change_star(self):
    self.star = not self.star
    return self.star

  def count_tasks(self):
    ct = 0
    for child in self.children:
      if isinstance(child, Task):
        ct+=1
    return ct
  
  def count_notes(self):
    nt = 0
    for child in self.children:
      if isinstance(child, Note):
        nt+=1
    return nt

  def count_checked_tasks(self):
    ctc = 0
    for child in self.children:
      if isinstance(child, Task):
        if child.check: 
          ctc+=1
    return ctc

  def count_started_tasks(self):
    cts = 0
    for child in self.children:
      if isinstance(child, Task):
        if child.started: 
          cts+=1
    return cts
