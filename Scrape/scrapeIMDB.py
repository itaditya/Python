#!/home/adi/Python/Scrape/venv/bin/python
import requests
import bs4
print "\n"+"-"*120+"\n"+"-"*120

A=[[],[],[]]

print ("Welcome To IMDB List of Top Movies\n")
root_url = 'http://www.imdb.com'
index_url = root_url + '/chart/top'

response = requests.get( index_url )
soup = bs4.BeautifulSoup(response.text ,"html.parser")
# print soup.title.string
table_list=soup.find('table', class_='chart')
for row in table_list.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==5: #Only extract table body not heading
        A[0].append(cells[1].find('a').find(text=True))
        A[1].append(cells[2].find('strong').find(text=True))
        A[2]=root_url+str(A[2].append(cells[1].find('a').attrs.get('href')))

#To print the data received
num=int(input("Show the list of Top __ ?"))

for x in xrange(0,num):
    print (x+1),":: ",A[0][x]," ",A[1][x]," ","\n"

print "-"*120+"\n\n\n"+"-"*120+"\n\n\n\n"
