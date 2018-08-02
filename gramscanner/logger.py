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

      print(color + title + ' --> ' + Fore.WHITE + Style.BRIGHT + grade + Style.RESET_ALL, flush=True)

Logger = Logger()