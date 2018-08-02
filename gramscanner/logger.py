from colorama import Fore, Style

class Logger:
  def status(self, text):
    print(Fore.CYAN + text, flush=True)
    print(Style.RESET_ALL)

  def fail(self, text):
    print(Fore.RED + text, flush=True)
    print(Style.RESET_ALL)

  def print_grades(self, data):
    for course in data['courses']:
      if 'Consolidation' in course['title']:
        color = Fore.WHITE + Style.DIM
      elif '-' in course['grade']:
        color = Fore.YELLOW
      else:
        color = Fore.GREEN

      print(color + course['title'] + ' --> ' + Fore.WHITE + Style.BRIGHT + course['grade'] + Style.RESET_ALL, flush=True)

Logger = Logger()