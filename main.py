#!/usr/bin/python -W ignore::DeprecationWarning

import urllib.request
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
import pandas
import act
import sys
from bs4 import BeautifulSoup

url = "https://www.efestivals.co.uk/festivals/glastonbury/2024/lineup.shtml"
content = urllib.request.urlopen(url).read()
soup = BeautifulSoup(content, "html.parser")

acts = soup.find('div', {'id': 'panel5'})\
           .find_all('div', {'class': 'band'})

list(map((lambda x: print(act.Act.parseAct(x))), acts))

