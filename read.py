import os
import csv
from pathlib import Path

import utils
from tree.task import Task
from tree.note import Note
from tree.board import Board

def read_file(file_name):

  with open(file_name, 'r') as csv_file:
    file = csv.DictReader(csv_file, utils.HEADER_CSV, delimiter=';')

    #if file is empty return
    if os.path.getsize(Path(file_name))==0:
     return

    next(file) # skip header

    nodes = []
    for row in file:
      node = row['node']
      id = int(row['id'])
      date = float(row['date'])
      star = int(row['star'])
      text = row['text']
      
      if node == 'b':
        children = [] if not row['children'] else [int(i) for i in row['children'].split(',')]
        nodes.append(Board(id=id, text=text, date=date, star=star, children=children))
      
      elif node == 't':
        nodes.append(Task(
          id=id, text=text, date=date, star=star,
          check=int(row['check']),
          started=int(row['started']),
          priority=int(row['priority']),
        ))
        
      elif node == 'n':
        nodes.append(Note(id=id, text=text, date=date, star=star))
    
    return nodes
