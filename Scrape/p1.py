#!/home/adi/Python/Scrape/venv/bin/python
import requests
import bs4
print "\n\n\n\n"+"-"*120+"\n\n\n"+"-"*120
root_url = 'http://pyvideo.org'
index_url = root_url + '/category/50/pycon-us-2014'

# response = requests.get('http://docs.python-requests.org/en/master/user/quickstart/',"html.parser")
# soup = bs4.BeautifulSoup(response.text)

# def get_video_page_urls():
    
#     links=[]

#     # return  response.text
#     return [a.attrs.get('href') for a in soup.select('a.mini-repo-list-item a[href^=https://]')]
#      # return soup.prettify()
#     print soup.title
#      # return [a.attrs.get('class') for a in soup.select('a#download-button')]
# print get_video_page_urls(),"\n\n\n\n\n\n\n\n\n"



def googlesearch(searchfor):                                                                                                                                                                                       
    link = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % searchfor                                                                                                                              
    ua = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36'}                                                                
    payload = {'q': searchfor}                                                                                                                                                                                     
    response = requests.get(link, headers=ua, params=payload)
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    links=soup.find_all('div')
    print len(links)
    return [a.attrs.get('href') for a in soup.select('div a')]                                                                                                                                                     
    print soup                                                                                                                                                                                    

links = googlesearch('imdb')
print(len(links))
for i in links :
    print(i,"\n \n")

print "-"*120+"\n\n\n"+"-"*120+"\n\n\n\n"


# >>> import requests
# >>> payload = {'key1': 'value1', 'key2': 'value2'}
# >>> r = requests.post("http://yourposturl", data=payload)
# >>> print r.text
