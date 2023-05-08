import csv

from tree.task import Task
from tree.note import Note
from tree.board import Board

import utils

header_csv = ['node', 'id', 'date', 'star', 'text', 'children', 'check', 'started', 'priority']

def read_file(file_name):

  with open(file_name, 'r') as csv_file:
    file = csv.DictReader(csv_file, header_csv, delimiter=';')

    next(file) # skip header

    nodes = []
    for row in file:
      node = row['node']
      id = int(row['id'])
      date = float(row['date'])
      star = int(row['star'])
      text = row['text']
      
      if node == 'Board':
        print(id, type(row['children']), row['children'])
        children = [] if not row['children'] else [int(i) for i in row['children'].split(',')]
        nodes.append(Board(id=id, text=text, date=date, star=star, children=children))
      
      elif node == 'Task':
        nodes.append(Task(
          id=id, text=text, date=date, star=star,
          check=int(row['check']),
          started=int(row['started']),
          priority=int(row['priority']),
        ))
        
      elif node == 'Note':
        nodes.append(Note(id=id, text=text, date=date, star=star))
    
    return nodes

def write_file(file_name, node):
  with open(file_name, 'w') as csv_file:
    file = csv.DictWriter(csv_file, header_csv, delimiter=';')
    file.writeheader()
    save_recursive(file, node, [])
  

def save_recursive(file, current, visited):
  
  visited.append(current)
  
  write_row(file, current)

  if isinstance(current, Board):
    for child in current.children:
      if child not in visited:
        save_recursive(file, child, visited)


def write_row(file, node):
  children = ''

  if isinstance(node, Board):  
    children=','.join([str(child.id) for child in node.children])

  row = {
    header_csv[0]: utils.type_node(node),
    header_csv[1]: node.id,
    header_csv[2]: node.date,
    header_csv[3]: int(node.star),
    header_csv[4]: node.text,
    header_csv[5]: children,
    header_csv[6]: int(node.check) if isinstance(node, Task) else None,
    header_csv[7]: int(node.started) if isinstance(node, Task) else None,
    header_csv[8]: node.priority if isinstance(node, Task) else None,
  }

  file.writerow(row)  