#!/home/adi/Python/Scrape/venv/bin/python
import requests
import bs4
print "\n"+"-"*120+"\n"+"-"*120

A=[[],[],[],[],[],[],[]]


root_url = 'https://en.wikipedia.org/wiki/'
index_url = root_url + 'List_of_state_and_union_territory_capitals_in_India'

response = requests.get( index_url )
soup = bs4.BeautifulSoup(response.text ,"html.parser")
print soup.title.string
table_list=soup.find('table', class_='wikitable sortable plainrowheaders')
for row in table_list.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A[0].append(cells[0].find(text=True))
        A[1].append(states[0].find(text=True))
        A[2].append(cells[1].find(text=True))
        A[3].append(cells[2].find(text=True))
        A[4].append(cells[3].find(text=True))
        A[5].append(cells[4].find(text=True))
        A[6].append(cells[5].find(text=True))

print len(table_list)
for x in xrange(0,36):
    print A[0][x],"\t",A[1][x],"\t",A[2][x],"\t",A[3][x],"\t",A[4][x],"\t",A[5][x],"\t",A[6][x],"\n"

print "-"*120+"\n\n\n"+"-"*120+"\n\n\n\n"
