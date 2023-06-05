import argparse
from pathlib import Path 

import utils
import messages.messages as msg
from tree.tree import Tree

CURRENT_DIR = Path(__file__).parent.absolute()

PATH_DIRWORK = Path(str(Path.home())+'/my-tasks/')

CONTEXT_DIR = Path(str(PATH_DIRWORK)+'/context')

CONTEXT_TREE = Path(str(CONTEXT_DIR)+'/tree.context')

def main():

  parser = argparse.ArgumentParser(description='My Tasks')

  parser.add_argument('input', nargs='?', help='Node id or board name', type=str)
  parser.add_argument('--file', '-f', help='Tree context file', type=str)#metavar='<file>')
  parser.add_argument('--timeline', '-tl', help='Tasks timeline', action='store_true')
  parser.add_argument('--task', '-t', nargs='+', help='Create task', type=str)#metavar='<my_task>')
  parser.add_argument('--note', '-n', nargs='+', help='Create annotation', type=str)#metavar='<my_note>')
  parser.add_argument('--board', '-b', nargs='+', help='Create board', type=str)#metavar='<my_board>')
  parser.add_argument('--delete', '-d', nargs='+', help="Id's to be deleted", type=str)#metavar='int')
  parser.add_argument('--check', '-c', nargs='+', help='Check task', type=int)#metavar='int')
  parser.add_argument('--started', '-s', nargs='+', help='Started task', type=int)#metavar='int')
  parser.add_argument('--star', '-x', nargs='+', help='Star to task', type=int)#metavar='int')
  parser.add_argument('--priority', '-p', help='Change priority level', type=int)
  parser.add_argument('--edit', '-e', nargs='+', help='Edit text node', type=str)

  args = parser.parse_args()


  #check if work dir exists else create work dir 
  if not Path(PATH_DIRWORK).is_dir():
    Path(PATH_DIRWORK).mkdir(parents=True, exist_ok=True)
    Path(CONTEXT_DIR).mkdir(parents=True, exist_ok=True)
    open(CONTEXT_TREE,'w').close()

  if args.file:
    if not utils.only_one_arg('file', args.__dict__):
      print('use only --file command') #TODO create message
      return
    
    path_tree = Path(str(PATH_DIRWORK)+'/'+args.file)

    with open(CONTEXT_TREE, 'w') as context_tree:
      
      if not path_tree.is_file():
        open(path_tree, 'w').close()        
        print(msg.new_tree_create(path_tree))

      context_tree.write(path_tree.__str__())

  else:
      with open(CONTEXT_TREE, 'r') as file:
        path_tree = file.readline()
      
      if path_tree:
        tree=Tree(path_tree)
      else:
        print(msg.uninitialized_context())
        return

    
  if args.timeline:
    if not utils.only_one_arg('timeline', args.__dict__):
      print('use only --timeline command') #TODO create message
      return
    tree.timeline()
    
  # new task with or withuot priority level
  if args.task:
    if args.priority:
      tree.add(text=' '.join(args.task), type='task', input=args.input, priority=args.priority)
    else:
      tree.add(text=' '.join(args.task), type='task', input=args.input)
  
  # new task
  if args.note:    
    tree.add(text=' '.join(args.note), type='note', input=args.input)
  
  # new borad(subtask)
  if args.board:    
    tree.add(text=' '.join(args.board), type='board', input=args.input)

  # delete list of nodes
  if args.delete:
    tree.delete(ids=args.delete)

    
  # change text the node
  if args.edit:
    tree.change_text(input=args.input, text=' '.join(args.edit))


  # change priority level of a task
  if args.priority is not None and args.input is not None and args.task is None:
    tree.change_priority(input=args.input, priority=args.priority)


  # mark task as completed
  if args.check:
    tree.change_check(ids=args.check)


  # mark task as started
  if args.started:
    tree.change_started(ids=args.started)


  # mark task a starred
  if args.star:
    tree.change_star(ids=args.star)


  # print some tree node or all tree
  if args.input and utils.only_one_arg('input', args.__dict__):
      x = tree.search(args.input)
      if x:
        tree.print_tree(x)
  
  # if all arguments are empty, print the whole tree 
  if utils.all_args_are_empty(args.__dict__):
    tree.print_tree()


if __name__ == '__main__':
  main()


















