from urllib.request import urlopen 
from bs4 import BeautifulSoup 

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'lxml')

print(bsObj.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

'''
# prints all siblings of table tag 
for sibling in bsObj.find('table', {'id': 'giftList'}).tr.next_siblings:
	print(sibling)

# prints all children of the table tag 
for child in bsObj.find('table', {'id': 'giftList'}).children:
	print(child)

# extracts list of proper nouns contained in span.green tags 
nameList = bsObj.findAll('span', {'class': 'green'})

for name in nameList:
	# note: get_text() strips all text formatting; typically used last
	# want to preserve formatting for as long as possible
	print(name.get_text()) 
'''