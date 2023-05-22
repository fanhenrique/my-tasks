import argparse

from tree.tree import Tree

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

  if args.file:
    with open('my-tasks/trees.txt', 'w') as file:
      file.write(args.file)
  else:
    with open('my-tasks/trees.txt', 'r') as file:
      tree_name = file.readline()
    
    tree=Tree('my-tasks/'+tree_name)
  
    # print(args._get_kwargs())    
    
  if args.timeline:
    tree.timeline()
    
  # nova tarefa com ou sem nivel de prioridade
  if args.task:
    if args.priority:
      tree.add(text=' '.join(args.task), type='task', input=args.input, priority=args.priority)
    else:
      tree.add(text=' '.join(args.task), type='task', input=args.input)
  
  # nova nota
  if args.note:    
    tree.add(text=' '.join(args.note), type='note', input=args.input)
  
  #nova subtarefa
  if args.board:    
    tree.add(text=' '.join(args.board), type='board', input=args.input)

  #deleta todos os nodos
  if args.delete:
    tree.delete(ids=args.delete)

    
  # #change text the node
  if args.edit:
    tree.change_text(input=args.input, text=' '.join(args.edit))


  # #altera a prioridade de uma tarefa
  if args.priority is not None and args.input is not None and args.task is None:
    tree.change_priority(input=args.input, priority=args.priority)


  # #marca tarefa como concluída
  if args.check:
    tree.change_check(ids=args.check)


  # #marca tarefa como iniciada
  if args.started:
    tree.change_started(ids=args.started)


  # #marca tarefa com uma estrela
  if args.star:
    tree.change_star(ids=args.star)


  #printa nodos da árvore ou toda ela
  if (
    args.input
    and args.file is None
    and not args.timeline 
    and args.task is None 
    and args.note is None
    and args.board is None
    and args.delete is None
    and args.check is None
    and args.started is None
    and args.star is None
    and args.priority is None
    and args.edit is None
  ):
    x = tree.search(args.input)

    if x:
      tree.print_tree(x)
  # elif not args.id and not args.task and not args.note and not args.board and not args.delete:
  else:
    if (
      args.input is None
      and args.file is None
      and not args.timeline 
      and args.task is None 
      and args.note is None
      and args.board is None
      and args.delete is None
      and args.check is None
      and args.started is None
      and args.star is None
      and args.priority is None
      and args.edit is None
    ):
      tree.print_tree()


if __name__ == '__main__':
  main()


















