from bs4 import BeautifulSoup
import urllib2
import wget
import re

url = "http://parlamentare2016.bec.ro/candidati/candidaturi-depuse-la-birourile-electorale-de-circumscriptie"

county_links = []
party_links = []
pdfs = []

html_page = urllib2.urlopen(url)
soup = BeautifulSoup(html_page, "lxml")
for link in soup.findAll('a'):
    county_links.append(link.get('href'))

#print county_links

filtered_county_links = [k for k in county_links if 'candidaturi' in k]

#print filtered_county_links

for r in filtered_county_links:
    print r
    html_page = urllib2.urlopen(r)
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        party_links.append(link.get('href'))


filtered_party_links = [k for k in party_links if 'candidaturi' in k]

for ps in filtered_party_links:
    print ps
    html_page = urllib2.urlopen(ps)
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        pdfs.append(link.get('href'))

print pdfs

filtered_pdf_list = [k for k in pdfs if 'pdf' in k]

for file in filtered_pdf_list:
    print file
    filename = wget.download(file) 
    print ' Saved ', filename
