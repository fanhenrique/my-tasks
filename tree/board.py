from collections import deque

import messages.messages as msg
from .task import Task
from .note import Note
from .node import Node

class Board(Node):

  def __init__(self, id:int, text:str, children:deque=deque(), star:bool=False, date:float=None):
    super().__init__(id, text, star, date)
    self.children = children #subtasks path or tasks or notes
    

  def __str__(self, level:int=0, info:tuple=None, show_date:bool=False):
    return super().__str__(      
      core=msg.board(self.text) + (msg.info(info[0], info[1]) if info else ''),
      level=level,
      show_date=show_date
    )


  def count_tasks(self):
    ct = 0
    for child in self.children:
      if isinstance(child, Task):
        ct+=1
    return ct


  def count_tasks_priority0(self):
    ctp0 = 0
    for child in self.children:
      if isinstance(child, Task):
        if child.priority == 0 and not child.check and not child.started:
          ctp0+=1
    return ctp0


  def count_tasks_priority1(self):
    ctp1 = 0
    for child in self.children:
      if isinstance(child, Task):
        if child.priority == 1 and not child.check and not child.started:
          ctp1+=1
    return ctp1


  def count_tasks_priority2(self):
    ctp2 = 0
    for child in self.children:
      if isinstance(child, Task):
        if child.priority == 2 and not child.check and not child.started:
          ctp2+=1
    return ctp2


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
