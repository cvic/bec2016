from bs4 import BeautifulSoup
import urllib2
import wget

url = "http://parlamentare2016.bec.ro/candidati/candidaturi-depuse-la-birourile-electorale-de-circumscriptie"

county_links = []
party_links = []
pdfs = []

html_page = urllib2.urlopen(url)
soup = BeautifulSoup(html_page, "lxml")
for link in soup.findAll('a'):
    county_links.append(link.get('href'))

filtered_county_links = [cl for cl in county_links if cl.count("/") == 6]

for link in filtered_county_links:
    html_page = urllib2.urlopen(link)
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        party_links.append(link.get('href'))

filtered_party_links = [pl for pl in party_links if pl.count("/") == 7]

#print filtered_party_links

for link in filtered_party_links:
    html_page = urllib2.urlopen(link)
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        pdfs.append(link.get('href'))

filtered_pdf_list = [pdf for pdf in pdfs if 'uploads' in pdf]

for file in filtered_pdf_list:
    print file
    filename = wget.download(file)
    print ' Saved ', filename
