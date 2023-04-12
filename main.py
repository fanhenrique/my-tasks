import argparse
import logging

from board import Board
from task import Task
from note import Note
from tree import Tree

DEFAULT_LOG_LEVEL = logging.INFO
TIME_FORMAT = '%Y-%m-%d,%H:%M:%S'

def main():

  parser = argparse.ArgumentParser(description='My Todos')

  parser.add_argument("--task", "-t", nargs='+', help="Create task", type=str)
  parser.add_argument("--note", "-n", nargs='+', help="Create annotation", type=str)
  parser.add_argument("--board", "-b", nargs='+', help="Create board", type=str)
  
  
  help_msg = "Logging level (INFO=%d DEBUG=%d)" % (logging.INFO, logging.DEBUG)
  parser.add_argument("--log", "-l", help=help_msg, default=DEFAULT_LOG_LEVEL, type=int)
  
  args = parser.parse_args()
  
  if args.log == logging.DEBUG:
    logging.basicConfig(format='%(asctime)s %(levelname)s {%(module)s} [%(funcName)s] %(message)s', datefmt=TIME_FORMAT, level=args.log)
  else:
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt=TIME_FORMAT, level=args.log)
    
  args = parser.parse_args()

  # tree = Tree(Node(id=0, text='MyTasks')))

  tree = Tree(
          Board(id=1, text='quadro1', childrens=[
            Board(id=2, text='quadro2', childrens = [
              Task(id=5, text='tarefa1', check=True),
              Note(id=6, text='nota1'),
              Board(id=7, text='quadro3', childrens = [
                Task(id=8, text='tarefa3', priority=1),
                Note(id=9, text='nota3')
              ]),
            ]),
            Task(id=3, text='tarefa2', priority=2),
            Note(id=4, text='nota2'),
          ])
        )

  node, path = tree.search(7)
    
  print(node.id if node else None, path)

  tree.print_tree()

  tree.add_node(Note(id=10, text='nota4'), path)

  tree.print_tree()


  # for b in args.board:
  #   tree.b 



if __name__ == '__main__':
  main()


















