import re
import codecs
import requests
from bs4 import BeautifulSoup
from halo import Halo
from colorama import Fore, Style

class GramScanner:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.login_URL = 'http://gram-web.ionio.gr/unistudent/login.asp'
    self.request_URL = 'http://gram-web.ionio.gr/unistudent/stud_CResults.asp?lang=en-us&studPg=1&mnuid=mnu3'
    self.headers = {
      'Referer': 'http://gram-web.ionio.gr/unistudent/login.asp',
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
      'Accept-Language': 'en-US,en;q=0.9'
    }
    self.logger = Halo(text= Style.DIM + 'Fetching login page...', spinner='dots')

  def get_grades(self):
    self.logger.start()
    for i in range(3):
      session = requests.Session()
      session.headers.update(self.headers)
      
      try:
        login_page = self.get_login_page(session)
      except Exception as e:
        self.logger.fail(text = Style.DIM + str(e))
        raise SystemExit

      try: 
        payload = self.get_payload(login_page)
        self.logger.succeed(text= Style.DIM + 'Successfully retrieved authentication tokens.')
        break
      except Exception as e:
        self.logger.fail(text= Style.DIM + str(e))
        if i == 2:
          raise SystemExit 
        self.logger.start(text= Style.DIM + 'Retrying...')
    
    self.logger.start(text = Style.DIM + 'Logging in on GramWeb')
    try:
      grades_page = self.get_grades_page(session, payload)
      self.logger.succeed(text= Style.DIM + 'Successfully logged in on GramWeb.')
    except Exception as e:
      self.logger.fail(text = Style.DIM + str(e))
      raise SystemExit
    
    self.logger.stop()

    return self.find_grades(grades_page)

    
  def get_payload(self, login_page):
    scripts = login_page.find_all('script')
    script = scripts[10].string.replace("'+'", "")

    matches = re.findall(r"\'(.+?)\'",script)
    name = self.hex_to_string(matches[0])
    
    if ('<input' in name or len(matches)<2):
      raise Exception('Failed retrieving authentication tokens.')
    
    value = self.hex_to_string(matches[1])

    return {
      'userName': self.username,
      'pwd': self.password,
      'submit1': 'Login',
      'loginTrue': 'login',
      name: value
    }

  def get_login_page(self, session):
    res = session.get(self.login_URL)
    res.encoding = 'windows-1253'

    return BeautifulSoup(res.text, "html.parser")

  def get_grades_page(self, session, payload):
    session.post(self.login_URL, data=payload)
    res = session.get(self.request_URL)
    res.encoding = 'windows-1253'

    if "Student Login" in res.text:
      raise Exception ("Failed logging in on GramWeb. Either your username or password is wrong.")

    if "Σφάλμα" in res.text:
      raise Exception ("An error occured on GramWeb please try again later.")

    return BeautifulSoup(res.text, "html.parser")

  def find_grades(self, grades_page):
    courses = []
    courses_table = grades_page.find_all('tr', bgcolor="#fafafa", height="25")

    for course in courses_table:
      values = course.find_all("td")
      c_title = " ".join(values[1].text.split())
      c_type = values[2].text.strip() 
      c_hours = values[4].text.strip()
      c_ects = values[5].text.strip()
      c_grade = values[6].span.text.strip()
      
      courses.append({
        'title': c_title,
        'type': c_type,
        'hours': c_hours,
        'ects': c_ects,
        'grade': c_grade
      })
    
    return {
      'courses': courses
    }
      
  def print_grades(self, data):
    for course in data['courses']:
      if 'Consolidation' in course['title']:
        color = Fore.WHITE + Style.DIM
      elif '-' in course['grade']:
        color = Fore.YELLOW
      else:
        color = Fore.GREEN

      print(color + course['title'] + ' --> ' + Fore.WHITE + Style.BRIGHT + course['grade'])
    
  def hex_to_string(self, value):
    return codecs.decode(value, 'unicode-escape').encode('latin1').decode('utf-8')
