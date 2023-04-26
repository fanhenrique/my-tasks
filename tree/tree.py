from collections import deque

import colored as colored

from tree.board import Board
from tree.task import Task
from tree.note import Note

class Tree():

  def __init__(self, root=None):
    self.root = Board(id=1, text='quadro1',
                  childrens = deque([
                    Task(id=12, text='tarefa6', started=True),              
                    Board(id=2, text='quadro2',
                      childrens = deque([
                        Task(id=5, text='tarefa1'),
                        Task(id=17, text='tarefa10', priority=1),
                        Task(id=10, text='tarefa4', started=True),
                        Board(id=7, text='quadro3', star=True,
                          childrens = deque([
                            Task(id=11, text='tarefa5', check=True),
                            Task(id=8, text='tarefa3', priority=1, started=True),
                            Task(id=16, text='tarefa11', priority=2, started=True),
                            Note(id=9, text='nota3', star=True)
                          ])
                        ),                
                        Task(id=13, text='tarefa7', priority=1, check=True),
                        Task(id=18, text='tarefa9', priority=1),
                        Note(id=6, text='nota1'),
                      ])
                    ),
                    Board(id=14, text='quadro4',
                      childrens = deque([
                        Task(id=15, text='tafera8', check=True)
                      ])
                    ),
                    Task(id=3, text='tarefa2', priority=2, star=True),
                    Note(id=4, text='nota2'),
                  ]),
                )
        

  def add(self, text, type, current=None):
    if not current:
      current = self.root
    
    new = None
    if type == 'note': 
      new = Note(id=20, text=text)
    elif type == 'task': 
      new = Task(id=20, text=text)
    elif type == 'board': 
      new = Board(id=20, text=text)

    if isinstance(current, Board):
      current.childrens.append(new)
      print(colored.confirmation_add(True, new))
    else:
      print(colored.confirmation_add(False, new))

    
    
  def _search(self, current, id, visited):

    visited.append(current)

    if current.id == id:
      return current

    a = None
    if isinstance(current, Board):
      for child in current.childrens:
        if child not in visited:
          a = self._search(child, id, visited)
          if a:
            break
    return a
    
  def search(self, current, id):
    if not current:
      current = self.root
    
    return self._search(current, id, [])


  def print_tree_iterative(self, current=None):

    if not current:
      current = self.root

    level = 0
    stack = deque([])
    visited = [current]
    stack.append((current, level))  
    while stack:
      
      current, level_current = stack.pop()
      
      print(current.__str__(level=level_current))

      if isinstance(current, Board):
        for child in reversed(current.childrens):
          if child not in visited:
            visited.append(child)
            stack.append((child, level_current+1))

  
  def _count_info_recursive(self, current, visited, func):
    
    visited.append(current)

    if isinstance(current, Board):
      x = 0
      for child in current.childrens:
        if child not in visited:
          x += self._count_info_recursive(child, visited, func)
      a = getattr(current, func)()
      return a + x
    
    return 0


  def print_tree_with_info_recursive(self, current, visited, level):
    
    visited.append(current)

    if isinstance(current, Board):
      print(current.__str__(level=level, info=[
          str(self._count_info_recursive(current, [], 'count_checked_tasks')),
          str(self._count_info_recursive(current, [], 'count_tasks')),
        ], date=True))
      
      for child in current.childrens:
        if child not in visited:
          self.print_tree_with_info_recursive(child, visited, level+1) 
    else:
      print(current.__str__(level, date=True))
  

  def print_tree(self, current):

    self.print_tree_with_info_recursive(current, [], 0)

    a = (
      self._count_info_recursive(current, [], 'count_tasks'),
      self._count_info_recursive(current, [], 'count_checked_tasks'),
      self._count_info_recursive(current, [], 'count_started_tasks'),            
      self._count_info_recursive(current, [], 'count_notes'),      
    )

    complete=a[1]*100/(a[0])
    
    print(colored.all_tree_info(
      complete,
      done=a[1], 
      pending=a[0]-a[1],
      started=a[2],
      not_started=a[0]-(a[1]+a[2]),
      notes=a[3],
    ))
    
    

    