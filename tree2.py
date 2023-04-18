from collections import deque

import colored

from board2 import Board2
from task import Task
from note import Note

class Tree2():
  def __init__(self, root):
    self.root = root

  # def add_node(self, current, new_node, path):
  
  #   current.childrens.append(new_node)
  
  # PRINTA ARVORE DE FORMA RECURSIVA
  # def print_recursive_dfs(self, current, visited, level):
  #   visited.append(current)
  #   # print(current)#, [child.id for child in current.childrens] if hasattr(current, 'childrens') else '')
  #   print('  '*level+current.__str__())
  #   if hasattr(current, 'childrens'):
  #     for child in current.childrens:
  #       if child not in visited:
  #           self.print_recursive_dfs(child, visited, level+1)


  # def search_dfs(self, id, current=None):
  #   if not current:
  #     current = self.root

  #   if current.id == id:
  #     return current, [current.id]

  #   path = []
  #   stack = deque([])
  #   visited = [current]
  #   stack.append(current)
  #   searrch_flag = True
    
  #   while stack and searrch_flag:

  #     current = stack.pop()
  #     if isinstance(current, Board):
  #       path.append(current.id)

  #     if isinstance(current, Board):
 
  #       for child in reversed(current.childrens):
          
  #         if child.id == id:
  #           path.append(child.id)
  #           searrch_flag = False
  #           break
      
  #         if child not in visited:
  #           visited.append(child)
  #           stack.append(child)

  #   if searrch_flag:
  #     return None, []
    
  #   return child, path


  # def count_info(self, current=None, level=0):
  #   if not current:
  #     current = self.root
  #   stack = deque([])
  #   visited = [current]
  #   stack.append(current)

  #   count_checks = 0
  #   count_tasks = 0
  #   count_notes = 0

  #   while stack:
  #     current = stack.pop()
  #     print(tc.colored('|  '*level,color='dark_grey', attrs=['dark'])+current.__str__(), '('+repr(count_checks)+'/'+repr(count_tasks)+')')
  #     # count_checks+=current.count_tasks_checks()
  #     if isinstance(current, Task):
  #       count_tasks+=1#current.count_tasks()
  #       if current.check:
  #         count_checks+=1
  #     if isinstance(current, Note):
  #       count_notes+=1#current.count_notes()

  #     if isinstance(current, Board):
        
  #       for child in current.childrens:
  #         if child not in visited:
  #           visited.append(child)
  #           stack.append(child)
    
  #   print(count_checks, count_tasks, count_notes)


  # def count_info_recursive(self, current, visited, level, cl):
  #   visited.append(current)
  #   # print(current)#, [child.id for child in current.childrens] if hasattr(current, 'childrens') else '')
  #   # print('|  '*level+current.__str__())

  #   print(tc.colored('|  '*level,color='dark_grey', attrs=['dark'])+current.__str__())
    
  #   if isinstance(current, Board):
  #     x = 0
  #     for child in current.childrens:
  #       if child not in visited:
  #         x += self.count_info_recursive(child, visited, level+1, cl) 
  #     # print('  '*level,x)
  #     print('t=', current.count_tasks(), 'x=', x)
  #     return x
  #   else:
  #     if isinstance(current, cl):
  #       return 1
  #     else:
  #       return 0

  # def count_info_recursive2(self, current, visited, level, cl):
  #   visited.append(current)
  #   # print(current.id, [child.id for child in current.childrens] if isinstance(current, Board) else '')
  #   # print('|  '*level+current.__str__())
  #   # print(current.id)

  #   if isinstance(current, Board):
  #     x=0
  #     for child in current.childrens:
  #       if child not in visited:
  #         x += self.count_info_recursive2(child, visited, level+1, cl) 
        
  #     print(tc.colored('|  '*level,color='dark_grey', attrs=['dark'])+current.__str__())
  #     print('t=', current.count_tasks(), 'x=', x)
  #     for child in current.childrens:
  #       if not isinstance(child, Board):   
  #         print(tc.colored('|  '*(level+1),color='dark_grey', attrs=['dark'])+child.__str__())
      
  #     return current.count_tasks() + x
        
  #   if not isinstance(current, Board):
  #     # print(tc.colored('|  '*(level+1),color='dark_grey', attrs=['dark'])+current.__str__())
  #     return 0


  def print_dfs(self, current=None):

    if not current:
      current = self.root

    level = 0
    stack = deque([])
    visited = [current]
    stack.append((current, level))  
    while stack:
      
      current, level_current = stack.pop()
      
      print(current.__str__(level_current))

      for task in current.tasks:
        print(task.__str__(level_current+1))

      for note in current.notes:
        print(note.__str__(level_current+1))

      for child in reversed(current.childrens):
        if child not in visited:
          visited.append(child)
          stack.append((child, level_current+1))

  
  def count_info_recursive(self, current, visited, func):
    
    visited.append(current)

    x = 0
    for child in current.childrens:
      if child not in visited:
        x += self.count_info_recursive(child, visited, func)
    a = getattr(current, func)()
    return a + x

  def print_info_recursive(self, current, visited, level, cl):
    
    visited.append(current)
      
    if isinstance(current, Board2):
      print(current.__str__(level=level, info=[
          str(self.count_info_recursive(current, [], 'count_tasks_checks')),
          str(self.count_info_recursive(current, [], 'count_tasks'))
        ]))

    for task in current.tasks:
      print(task.__str__(level+1))

    for note in current.notes:
      print(note.__str__(level+1))
    
    for child in current.childrens:
      if child not in visited:
        self.print_info_recursive(child, visited, level+1, cl) 

                
    
    

  # def bfs(self, current):
  #   level = 0
  #   queue = deque([])
  #   visited = []
  #   queue.append((current, level))
  #   while queue:
  #     current, level_current = queue.popleft()
  #     # print(current, [child.id for child in current.childrens] if hasattr(current, 'childrens') else '')
  #     print('  '*level_current+current.__str__(), level_current)
  #     level=level_current+1
  #     if current not in visited:
  #       visited.append(current)
  #       if hasattr(current, 'childrens'):
  #         queue.extend([(child, level) for child in current.childrens])
      
        













    