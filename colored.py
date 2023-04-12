import termcolor as tc

def colored_id(id):
  return tc.colored(text=repr(id), color='dark_grey', attrs=['bold']) + tc.colored('. ', color='dark_grey')
