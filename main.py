#!/usr/bin/python

import urllib.request
import pandas
import act
import sys
from bs4 import BeautifulSoup

url = "https://www.efestivals.co.uk/festivals/glastonbury/2019/lineup.shtml"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")

acts = soup.find('div', {'id': 'panel1'})\
           .find_all('div', {'class': 'band'})

list(map((lambda x: print(act.Act.parseAct(x))), acts))

print(len(acts), "acts found in total.\n")
