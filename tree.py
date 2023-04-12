from collections import deque
import termcolor as tc

from board import Board

class Tree():
  def __init__(self, root):
    self.root = root

  def add_node(self, new_node, path):
    
    current = self.root
    
    

    # print([child.id for child in current.childrens])  
    # current = current.childrens[0]
    

    # print(current.id)
    for i in range(len(path)):
      child, _ = self.search(path[-1])
      
      if isinstance(child, Board):
        child.childrens.append(new_node)


      
    # if current.id == path[-1]:
      # current.childrens.append(new_node)

    # print(current.id)
    

  def search(self, id):
    if not self.root:
      return None

    return self.search_dfs(self.root, id)

  def print_tree(self):
    if not self.root:
      return None

    self.print_dfs(self.root)
    print('--------------------')
    
  
  # PRINTA ARVORE DE FORMA RECURSIVA
  # def print_recursive_dfs(self, current, visited, level):
  #   visited.append(current)
  #   # print(current)#, [child.id for child in current.childrens] if hasattr(current, 'childrens') else '')
  #   print('  '*level+current.__str__())
  #   if hasattr(current, 'childrens'):
  #     for child in current.childrens:
  #       if child not in visited:
  #           self.print_recursive_dfs(child, visited, level+1)


  def search_dfs(self, current, id):

    if current.id == id:
      return current, [current.id]

    path = []
    stack = deque([])
    visited = [current]
    stack.append(current)
    searrch_flag = True
    
    while stack and searrch_flag:

      current = stack.pop()
      if isinstance(current, Board):
        path.append(current.id)

      if isinstance(current, Board):
 
        for child in reversed(current.childrens):
          
          if child.id == id:
            searrch_flag = False
            break
      
          if child not in visited:
            visited.append(child)
            stack.append(child)

    if searrch_flag:
      return None, []
    
    return child, path

  def print_dfs(self, current):
    level = 0
    stack = deque([])
    visited = [current]
    stack.append((current, level))  
    while stack:
      
      current, level_current = stack.pop()
      # print(current, [child.id for child in current.childrens] if hasattr(current, 'childrens') else '')
      print(tc.colored('|  '*level_current,color='dark_grey', attrs=['dark'])+current.__str__())
      
      if isinstance(current, Board):
        
        level=level_current+1

        for child in reversed(current.childrens):
          if child not in visited:
            visited.append(child)
            stack.append((child, level))


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
      
        













    