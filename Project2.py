from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import re

html_page= urllib2.urlopen("https://www.google.co.in")
soup=BeautifulSoup(html_page)
images=[]
for img in soup.findAll('img'):
	images.append(img.get('src'))
print (images)
urllib.urlretrieve(images, "File.txt")
raw_input()