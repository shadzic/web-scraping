# -*- coding: utf-8 -*-
"""
Created on Fri Jan 02 13:34:17 2015

@author: Selma Hadzic
"""
from lxml import html
import requests
# Example : http://docs.python-guide.org/en/latest/scenarios/scrape/s
page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.text)
#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')



# Scraping weather forecast in Paris
page2 = requests.get('http://www.meteo-paris.com/')
tree2 = html.fromstring(page2.text)
temperatures = tree2.xpath('//div[@class="ac_temp"]/text()')
temperatures_b = list()
for i in range(len(temperatures)):
    temperatures_b.append(temperatures[i].encode("UTF-8").split()[0])
date_jour = tree2.xpath('//span[@id="date_accueil"]/text()')[1]
prevision_fete = tree2.xpath('//span[@class="prevision_fete"]/text()')
fete_jour = prevision_fete[0].split('/')[0].strip()

print "Aujourd'hui " + date_jour.lower() + ", c'est la " + fete_jour + ". Il fera " + temperatures_b[0] + " degrés le matin, puis " + temperatures_b[1] + " degrés l'après-midi et " + temperatures_b[2] + " degrés en soirée."

# Send a warning email in case of rain probability higher than 70%
rain_risk = tree2.xpath('//span[@class="pourcent"]/text()')
#if rain_risk[0].split('%')[0] >= 70:
#  sendTextMail()   
    
    








