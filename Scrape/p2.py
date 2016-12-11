#!/home/adi/Python/Scrape/venv/bin/python
import requests
import bs4
print "\n\n\n\n"+"-"*120+"\n\n\n"+"-"*120
def ncsreq(name,mobile,admno,mail,y,w):                                                                                                                                                                                       
    link = 'http://hackncs.com/register'                                                                                                                              
    payload = {
        'name': name,
        'mobile' :mobile,
        'admission_number' : admno,
        


    };                                                                                                                                                                                     
    response = requests.get(link, headers=ua, params=payload)
    soup = bs4.BeautifulSoup(response.text)                                                                                                                                                      
    print soup                                                                                                                                                                                    

ncsreq('Aditya','9911502984','15CS006','adityaa803@gmail.com','Yes','Web Club')

print "-"*120+"\n\n\n"+"-"*120+"\n\n\n\n"