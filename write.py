import csv

import utils
from tree.task import Task
from tree.board import Board

def write_file(file_name, node):
  with open(file_name, 'w') as csv_file:
    file = csv.DictWriter(csv_file, utils.HEADER_CSV, delimiter=';')
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
  if not node:
    return
  
  children = ''

  if isinstance(node, Board):  
    children=','.join([str(child.id) for child in node.children])

  row = {
    utils.HEADER_CSV[0]: utils.string_type_node(node),
    utils.HEADER_CSV[1]: node.id,
    utils.HEADER_CSV[2]: node.date,
    utils.HEADER_CSV[3]: int(node.star),
    utils.HEADER_CSV[4]: node.text,
    utils.HEADER_CSV[5]: children,
    utils.HEADER_CSV[6]: int(node.check) if isinstance(node, Task) else None,
    utils.HEADER_CSV[7]: int(node.started) if isinstance(node, Task) else None,
    utils.HEADER_CSV[8]: node.priority if isinstance(node, Task) else None,
  }

  file.writerow(row)
