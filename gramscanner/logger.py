import sys
from colorama import Fore, Style

class Logger:
  def __init__ (self, logger):
    self.logger = logger

  def status(self, text):
    if self.logger:
      sys.stdout.write(Fore.CYAN)
      sys.stdout.write(text)
      sys.stdout.write(Style.RESET_ALL)
      sys.stdout.write('\n')
      sys.stdout.flush()

  def fail(self, text):
    sys.stdout.write(Fore.RED)
    sys.stderr.write(text)
    sys.stdout.write(Style.RESET_ALL)
    sys.stdout.write('\n')
    sys.stdout.flush()
    
  def print_grades(self, data):
    for course in data['courses']:
      title = course['title']
      grade = course['grade']

      if 'Consolidation' in course['title']:
        color = Fore.WHITE + Style.DIM
      elif '-' in grade:
        color = Fore.YELLOW
      elif int(grade)<5:
        color = Fore.RED
      else:
        color = Fore.GREEN

      sys.stdout.write(color)
      sys.stdout.write(title + ' --> ' + Fore.WHITE + Style.BRIGHT + grade)
      sys.stdout.write(Style.RESET_ALL)
      sys.stdout.write('\n')
      sys.stdout.flush()