from collections import deque

import colored as colored

from tree.board import Board
from tree.task import Task
from tree.note import Note

import utils 

class Tree():

  def __init__(self, file):
    self.root = self.read(file)
    # self.root = Board(id=1, text='quadro1',
    #               children = deque([
    #                 Task(id=12, text='tarefa6', started=True),              
    #                 Board(id=2, text='quadro2',
    #                   children = deque([
    #                     Task(id=5, text='tarefa1'),
    #                     Task(id=17, text='tarefa10', priority=1),
    #                     Task(id=10, text='tarefa4', started=True),
    #                     Board(id=7, text='quadro3', star=True,
    #                       children = deque([
    #                         Task(id=11, text='tarefa5', check=True),
    #                         Task(id=8, text='tarefa3', priority=1, started=True),
    #                         Task(id=16, text='tarefa11', priority=2, started=True),
    #                         Note(id=9, text='nota3', star=True)
    #                       ])
    #                     ),                
    #                     Task(id=13, text='tarefa7', priority=1, check=True),
    #                     Task(id=18, text='tarefa9', priority=1),
    #                     Note(id=6, text='nota1'),
    #                   ])
    #                 ),
    #                 Board(id=14, text='quadro4',
    #                   children = deque([
    #                     Task(id=15, text='tafera8', check=True)
    #                   ])
    #                 ),
    #                 Task(id=3, text='tarefa2', priority=2, star=True),
    #                 Note(id=4, text='nota2'),
    #               ]),
    #             )
        

  def add(self, text, type, id):
    
    if id == None:
      current = self.root
    else:
      current = self.search(id)
    if not current:
      return

    if type == 'note': 
      new = Note(id=20, text=text) #TODO depois verificar primeiro id disponível
    elif type == 'task': 
      new = Task(id=20, text=text) #TODO depois verificar primeiro id disponível
    elif type == 'board': 
      new = Board(id=20, text=text) #TODO depois verificar primeiro id disponível

    if isinstance(current, Board):
      current.children.append(new)
      print(colored.confirmation_add(confirmation=True, new=new))
    else:
      print(colored.confirmation_add(confirmation=False, father=current, new=new))

    
  def change_priority(self, id, priority):

    try:
      node = self.search(id)

      if isinstance(node, Task):
        node.change_priority(priority)
        print(colored.confirmation_change(node))        
      elif node:
        print(colored.only_tasks_have_priority(node))
        
    except IndexError:
      print(colored.priority_level_out_of_range())
      

  def change_started(self, ids):
    
    for id in ids:
      node = self.search(id)
      
      if isinstance(node, Task):
        node.change_started()
      elif node:
        print(colored.only_tasks_can_be_started(node))
  

  def change_check(self, ids):
    
    for id in ids:
      node = self.search(id)
      
      if isinstance(node, Task):
        node.change_check()
      elif node:
        print(colored.only_tasks_can_be_checked(node))


  def change_star(self, ids):
    for id in ids:
      node = self.search(id)

      if node:
        node.change_star()


  def _depth_fist_delete_recursive(self, current, visited, nodes_to_delete):
    
    visited.append(current)
    
    if isinstance(current, Board):
      deleted = []
      for child in current.children:      
        if child not in visited:
          if self._depth_fist_delete_recursive(child, visited, nodes_to_delete):
            deleted.append(child)
    
      for child in deleted:
        current.children.remove(child)
        print(colored.confirmation_delete(child))

    if current in nodes_to_delete:
      return True

    return False


  def delete(self, ids=[]):
    
    #check if ids node is tree
    nodes_to_delete = []
    for id in ids:
      nodes_to_delete.append(self.search(id))
      
    self._depth_fist_delete_recursive(self.root, [], nodes_to_delete)
    
    #if id root in ids deleted 
    if self.root.id in ids:
      print(colored.confirmation_delete(self.root))
      self.root = None


  def _depth_first_search_father_recursive(self, current, id, visited):
  
    visited.append(current)  

    a = None
    if isinstance(current, Board):
      for child in current.children:
        if child.id == id:
          return current
      for child in current.children:    
        if child not in visited:          
          a = self._depth_first_search_father_recursive(child, id, visited)
          if a:
            break
    return a


  def _depth_first_search_recursive(self, current, id, visited):

    visited.append(current)

    if current.id == id:
      return current
   
    if isinstance(current, Board):
      for child in current.children:
        if child not in visited:
          a = self._depth_first_search_recursive(child, id, visited)
          if a:
            return a
    return None
    

  def search(self, id):
    
    dfs = self._depth_first_search_recursive(self.root, id, [])

    if not dfs:
      print(colored.id_not_found(id))
      return None

    return dfs


  # def print_tree_iterative(self, current=None):

  #   if not current:
  #     current = self.root

  #   level = 0
  #   stack = deque([])
  #   visited = [current]
  #   stack.append((current, level))  
  #   while stack:
      
  #     current, level_current = stack.pop()
      
  #     print(current.__str__(level=level_current))

  #     if isinstance(current, Board):
  #       for child in reversed(current.children):
  #         if child not in visited:
  #           visited.append(child)
  #           stack.append((child, level_current+1))

  
  def _depth_first_count_info_recursive(self, current, visited, func):
    
    visited.append(current)

    if isinstance(current, Board):
      x = 0
      for child in current.children:
        if child not in visited:
          x += self._depth_first_count_info_recursive(child, visited, func)
      a = getattr(current, func)()
      return a + x
    
    return 0


  def print_tree_with_info_recursive(self, current, visited, level):
    
    visited.append(current)

    if isinstance(current, Board):
      print(current.__str__(level=level, info=[
          str(self._depth_first_count_info_recursive(current, [], 'count_checked_tasks')),
          str(self._depth_first_count_info_recursive(current, [], 'count_tasks')),
        ], date=True))
      
      for child in current.children:
        if child not in visited:
          self.print_tree_with_info_recursive(child, visited, level+1) 
    else:
      print(current.__str__(level, date=True))
  

  def print_tree(self, start):
    if not start:
      return

    self.print_tree_with_info_recursive(start, [], 0)

    if isinstance(start, Board):

      a = (
        self._depth_first_count_info_recursive(start, [], 'count_tasks'),
        self._depth_first_count_info_recursive(start, [], 'count_checked_tasks'),
        self._depth_first_count_info_recursive(start, [], 'count_started_tasks'),            
        self._depth_first_count_info_recursive(start, [], 'count_notes'),      
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


  def _write(self, file, node):
    
    file.write(f'{utils.type_node(node)} {node.id} {node.text} {node.date} {int(node.star)}')

    if isinstance(node, Board):
      for child in node.children:
        file.write(f' {child.id}')
    elif isinstance(node, Task):
      file.write(f' {int(node.check)} {int(node.started)} {int(node.priority)}')

    file.write(' \n')
      

  def _save_recursive(self, file, current, visited):
    
    visited.append(current)
    
    self._write(file, current)

    if isinstance(current, Board):
      for child in current.children:
        if child not in visited:
          self._save_recursive(file, child, visited)
  
  def save(self, file):
    with open(file, 'w') as file:
      self._save_recursive(file, self.root, [])
      

  def _read_recursive(self, file):
    
    line = file.readline().split(' ')
    type = line[0]
    id = int(line[1])
    text = line[2]
    date = float(line[3])
    star = int(line[4])
    
    if type == 'Board':
      children = []
      for id_child in line[5:-1]:
        child = self._read_recursive(file)
        if child.id == int(id_child):
          children.append(child)
  
      node = Board(id=id, text=text, date=date, star=star, children=children)
    elif type == 'Task':
      node = Task(id=id, text=text, date=date, star=star, check=int(line[5]), started=int(line[6]), priority=int(line[7]))
    elif type == 'Note':
      node = Note(id=id, text=text, date=date, star=star)

    return node

  def read(self, file):
    with open(file, 'r') as file:
      return self._read_recursive(file)
     

        

    

