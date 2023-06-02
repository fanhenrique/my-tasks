import termcolor as tc

def colored(text:str, color:str, attrs:list[str]=None):
  return tc.colored(text, color=color, attrs=attrs)

def dark_grey_dark_bold(text:str):
  return tc.colored(text, color='dark_grey', attrs=['dark', 'bold'])

def light_grey_dark_bold(text:str):
  return tc.colored(text, color='light_grey', attrs=['dark', 'bold'])

def dark_grey_bold(text:str):
  return tc.colored(text, color='dark_grey', attrs=['bold'])

def dark_grey_dark(text:str):
  return tc.colored(text, color='dark_grey', attrs=['dark'])

def light_yellow(text:str):
  return tc.colored(text, color='light_yellow')

def green_bold(text:str):
  return tc.colored(text, color='green', attrs=['bold'])

def green_bold_underline(text:str):
  return tc.colored(text, color='green', attrs=['bold', 'underline'])

def magenta(text:str):
  return tc.colored(text, color='magenta')

def magenta_bold(text:str):
  return tc.colored(text, color='magenta', attrs=['bold'])

def light_red_bold(text:str):
  return tc.colored(text, color='light_red', attrs=['bold'])

def green_bold(text:str):
  return tc.colored(text, color='green', attrs=['bold'])

def white_bold(text:str):
  return tc.colored(text, color='white', attrs=['bold'])

def light_green_bold(text:str):
  return tc.colored(text, color='light_green', attrs=['bold'])

def blue_bold(text:str):
  return tc.colored(text, color='blue', attrs=['bold'])