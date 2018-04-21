#!/usr/bin/env python
import os
import re
import codecs

import click
import requests
from bs4 import BeautifulSoup
from halo import Halo
from colorama import Fore, Style

if "GramWebUser" in os.environ:
  pass
else:
  print (Style.DIM + "Please set the environment variable GramWebUser" + Style.NORMAL)
  raise SystemExit

if "GramWebPass" in os.environ:
  pass
else:
  print (Style.DIM + "Please set the environment variable GramWebPass")
  raise SystemExit

username = os.environ.get('GramWebUser')
password = os.environ.get('GramWebPass')

login_URL = 'http://gram-web.ionio.gr/unistudent/login.asp'
request_URL = 'http://gram-web.ionio.gr/unistudent/stud_CResults.asp?lang=en-us&studPg=1&mnuid=mnu3'
headers = {
  'Referer': 'http://gram-web.ionio.gr/unistudent/login.asp',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
  'Accept-Language': 'en-US,en;q=0.9'
}
@click.command()
def main():   
    spinner = Halo(text= Style.DIM + 'Fetching login page...', spinner='dots')
    spinner.start()
    
    for i in range(3):

      session = requests.Session()
      
      try:
        login_page = get_login_page(session)
      except Exception as e:
        spinner.fail(text=str(e))
        raise SystemExit

      try: 
        payload = getPayload(login_page)
        spinner.succeed(text= Style.DIM + 'Successfully retrieved hex values.')
        break
      except Exception as e:
        spinner.fail(text= Style.DIM + str(e))
        if i == 2:
          raise SystemExit 
        spinner.start(text= Style.DIM + 'Retrying...')
    
    spinner.start(text = Style.DIM + 'Logging in on GramWeb')
    try:
      grades_page = get_grades_page(session, payload)
      spinner.succeed(text= Style.DIM + 'Successfully logged in on GramWeb.')
    except Exception as e:
      spinner.fail(text = Style.DIM + str(e))
      raise SystemExit
    
    grades_soup = BeautifulSoup(grades_page, "html.parser")
    find_grades(grades_soup)
    
    spinner.stop()

def getPayload(login_page):
  scripts = login_page.find_all('script')
  script = scripts[10].string.replace("'+'", "")

  matches = re.findall(r"\'(.+?)\'",script)
  name = codecs.decode(matches[0], 'unicode-escape').encode('latin1').decode('utf-8')
  
  if ('<input' in name or len(matches)<2):
    raise Exception('Failed retrieving hex values.')
  
  value = codecs.decode(matches[1], 'unicode-escape').encode('latin1').decode('utf-8')

  return {
    'userName': username,
    'pwd': password,
    'submit1': 'Login',
    'loginTrue': 'login',
    name: value
  }

def get_login_page(session):
  req_header = session.headers.update(headers)
  l_response = session.get(login_URL)
  l_response.encoding = 'windows-1253'
  text = l_response.text

  return BeautifulSoup(text, "html.parser")

def get_grades_page(session, payload):
  post = session.post(login_URL, data=payload)
  r = session.get(request_URL)
  r.encoding = 'windows-1253'

  if "Student Login" in r.text:
    raise Exception ("Failed logging in on GramWeb. Either your username or password is wrong.")

  if "Σφάλμα" in r.text:
    raise Exception ("An error occured on GramWeb please try again later.")

  return r.text

def find_grades(grades_soup):
  lessons = grades_soup.find_all('tr', bgcolor="#fafafa", height="25")

  for lesson in lessons:
    values = lesson.find_all("td")
    l_title = " ".join(values[1].text.split())
    l_type = values[2].text.strip() 
    l_hours = values[4].text.strip()
    l_ects = values[5].text.strip()
    l_grade = values[6].span.text.strip()
    
    print_grades(l_title, l_grade)

def print_grades(l_title, l_grade):
  if 'Consolidation' in l_title:
    color = Fore.WHITE + Style.DIM
  elif '-' in l_grade:
    color = Fore.YELLOW
  else:
    color = Fore.GREEN

  print(color + l_title + ' --> ' + Fore.WHITE + Style.BRIGHT + l_grade)    

if(__name__ == "__main__"):
    main()
