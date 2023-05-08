from collections import deque
import csv

import colored as colored

from tree.board import Board
from tree.task import Task
from tree.note import Note

import utils 
import read_write as rw

class Tree():

  def __init__(self, file):
    self.file = file
    self.root = self.load(file)
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
    
    #search father
    father = self.search(id) if id else self.root
    
    if not father:
      return

    #create node
    if type == 'note': 
      new = Note(id=self._id_available(), text=text)
    elif type == 'task': 
      new = Task(id=self._id_available(), text=text)
    elif type == 'board': 
      new = Board(id=self._id_available(), text=text)

    # add new node in children of father
    if isinstance(father, Board):
      father.children.append(new)
      print(colored.confirmation_add(confirmation=True, new=new))
      self.save()
    else:
      print(colored.confirmation_add(confirmation=False, father=father, new=new))

    
  def change_priority(self, id, priority):

    try:
      node = self.search(id)

      if isinstance(node, Task):
        node.change_priority(priority)
        print(colored.confirmation_change_priority(node))
        self.save()
      elif node:
        print(colored.only_tasks_have_priority(node))
        
    except IndexError:
      print(colored.priority_level_out_of_range())
      

  def change_started(self, ids):
    
    for id in ids:
      node = self.search(id)
      
      if isinstance(node, Task):
        node.change_started()
        self.save()
      elif node:
        print(colored.only_tasks_can_be_started(node))
  

  def change_check(self, ids):
    
    for id in ids:
      node = self.search(id)
      
      if isinstance(node, Task):
        node.change_check()
        self.save()
      elif node:
        print(colored.only_tasks_can_be_checked(node))


  def change_star(self, ids):
    for id in ids:
      node = self.search(id)

      if node:
        node.change_star()
        self.save()


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
    
    #check if node ids in tree
    nodes_to_delete = []
    for id in ids:
      nodes_to_delete.append(self.search(id))
      
    self._depth_fist_delete_recursive(self.root, [], nodes_to_delete)
    
    #if root id is in deleted ids
    if self.root.id in ids:
      print(colored.confirmation_delete(self.root))
      self.root = None

    self.save()

  # def _depth_first_search_father_recursive(self, current, id, visited):
  
  #   visited.append(current)  

  #   a = None
  #   if isinstance(current, Board):
  #     for child in current.children:
  #       if child.id == id:
  #         return current
  #     for child in current.children:    
  #       if child not in visited:          
  #         a = self._depth_first_search_father_recursive(child, id, visited)
  #         if a:
  #           break
  #   return a


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
      
      complete=a[1]*100/(a[0]) if a[0] else 0
      
      print(colored.all_tree_info(
        complete,
        done=a[1], 
        pending=a[0]-a[1],
        started=a[2],
        not_started=a[0]-(a[1]+a[2]),
        notes=a[3],
      ))


  def save(self, file=None):
    if not file:
      file = self.file
    
    rw.write_file(file_name=file, node=self.root)


  def load(self, file):    
    
    nodes = rw.read_file(file_name=file)
    
    # mount adjacency
    for node in nodes:
      if isinstance(node, Board):        
        for id_child in node.children:
          for n in nodes:
            if id_child == n.id:
              node.children[node.children.index(id_child)] = n

    return nodes[0]


  def _ids_used(self, ids, current, visited):
    
    visited.append(current)
    ids.append(current.id)

    if isinstance(current, Board):
      for child in current.children:
        if child not in visited:
          self._ids_used(ids, child, visited)

    return ids


  def _id_available(self):    
    return utils.find_missing(self._ids_used([], self.root, []))
