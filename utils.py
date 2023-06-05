HEADER_CSV = ('node', 'id', 'date', 'star', 'text', 'children', 'check', 'started', 'priority')

# check if all arguments are empty
def all_args_are_empty(args:dict):
  for arg in args:
    if args[arg]:
      return False
  return True
    
# check if only are one argument
def only_one_arg(x:str, args:dict):
  
  flag = False
  for arg in args:
    if arg == x and args[arg]:
      flag = True
    if arg != x and args[arg]:
      return False

  return flag
