from collections import deque

import colored

from board import Board

class Tree():
  def __init__(self, root):
    self.root = root

  def add_node(self, new_node, current=None):
    if not current:
      current = self.root

    if isinstance(current, Board):  
      current.childrens.append(new_node)
      return True
    else:
      return False
    

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

  
  def count_info_recursive(self, current, visited, func):
    
    visited.append(current)

    if isinstance(current, Board):
      x = 0
      for child in current.childrens:
        if child not in visited:
          x += self.count_info_recursive(child, visited, func)
      a = getattr(current, func)()
      return a + x
    
    return 0

  def print_tree_with_info_recursive(self, current, visited, level):
    
    visited.append(current)

    if isinstance(current, Board):
      print(current.__str__(level=level, info=[
          str(self.count_info_recursive(current, [], 'count_checked_tasks')),
          str(self.count_info_recursive(current, [], 'count_tasks')),
          # str(self.count_info_recursive(current, [], 'count_notes')),
        ], date=True))
      

      for child in current.childrens:
        if child not in visited:
          self.print_tree_with_info_recursive(child, visited, level+1) 
    else:
      print(current.__str__(level, date=True))
  
    return (
      self.count_info_recursive(current, [], 'count_tasks'),
      self.count_info_recursive(current, [], 'count_checked_tasks'),
      self.count_info_recursive(current, [], 'count_started_tasks'),            
      self.count_info_recursive(current, [], 'count_notes'),      
    )

  def print_tree(self, current):

    a = self.print_tree_with_info_recursive(current, [], 0)

    complete=a[1]*100/(a[0])
    
    print(colored.all_tree_info(
      complete,
      done=a[1], 
      pending=a[0]-a[1],
      started=a[2],
      not_started=a[0]-(a[1]+a[2]),
      notes=a[3],
    ))
    
    

    