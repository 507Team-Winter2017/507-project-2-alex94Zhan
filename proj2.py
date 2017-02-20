#proj2.py
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')
rq = urllib.request.Request("https://www.nytimes.com/")
uhand = urllib.request.urlopen(rq)
html1 = uhand.read()
soup1 = BeautifulSoup(html1,'html.parser')
i = 1
for sh in soup1.find_all('h2', class_='story-heading'):
	if sh.a:
		print(sh.a.text.replace("\n","").strip())
	else:
		print(sh.contents[0].strip())
	i += 1
	if i == 11:
		break
### Your Problem 1 solution goes here


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
rq = urllib.request.Request("https://www.michigandaily.com/")
uhand = urllib.request.urlopen(rq)
html2 = uhand.read()
soup2 = BeautifulSoup(html2, 'html.parser')
for mr in soup2.find_all('div', class_='panel-pane pane-mostread'):
	for mr2 in mr.find_all('div', class_='item-list'):
		print(mr2.text.strip())

#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
rq = urllib.request.Request("http://newmantaylor.com/gallery.html")
uhand = urllib.request.urlopen(rq)
html3 = uhand.read()
soup3 = BeautifulSoup(html3, 'html.parser')
for image in soup3.find_all('img'):
	if image.get('alt'):
		print(image['alt'])
	else:
		print("No alternative text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
def GoToNext(obj):
	for li in obj.find_all('li', class_='pager-next last'):
		if li.text.strip():
			rs = "https://www.si.umich.edu"+li.a['href']
			return rs
	return
# print(GoToNext(BeautifulSoup(urllib.request.urlopen('https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page=5').read(), 'html.parser')))
# mysock.connect(('https://www.si.umich.edu', 80))
rq = urllib.request.Request("https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4", None, {'User-Agent': 'SI_CLASS'})
uhand = urllib.request.urlopen(rq)
html4 = uhand.read()
soup4 = BeautifulSoup(html4, 'html.parser')
next4 = ""
i = 1
while next4 or i == 1:
	for item in soup4.find_all('div',class_='field-item even'):
		if 'Contact Details' in item.text:
			nrq = urllib.request.Request("https://www.si.umich.edu"+item.a['href'],None, {'User-Agent': 'SI_CLASS'})
			unew = urllib.request.urlopen(nrq)
			htmlnew = unew.read()
			soupN = BeautifulSoup(htmlnew, 'html.parser')
			for item2 in soupN.find_all('div', class_='field-item even'):
				if '@umich.edu' in item2.text:
					print(i, item2.text)
					i += 1
	next4 = GoToNext(soup4)
	if next4:
		rq = urllib.request.Request(next4, None, {'User-Agent': 'SI_CLASS'})
		uhand = urllib.request.urlopen(rq)
		html4 = uhand.read()
		soup4 = BeautifulSoup(html4, 'html.parser')