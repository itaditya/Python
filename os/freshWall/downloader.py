from bs4 import BeautifulSoup
import subprocess
import urllib2
import os
import json


def get_soup(url, header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url, headers=header)), 'html.parser')


def scrapeGoogle(query):
    x = 0
    image_type = "ActiOn"
    query = query.split()
    query = '+'.join(query)
    url = "https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
    print url
    # add the directory for your image here
    DIR = "images/"
    header = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
              }
    soup = get_soup(url, header)

    ActualImages = []  # contains the link for Large original images, type of  image
    for a in soup.find_all("div", {"class": "rg_meta"}):
        link, Type = json.loads(a.text)["ou"], json.loads(a.text)["ity"]
        ActualImages.append((link, Type))

    print "there are total", len(ActualImages), "images"

    # print images
    for i, (img, Type) in enumerate(ActualImages):
        try:
            req = urllib2.Request(img, headers={'User-Agent': header})
            raw_img = urllib2.urlopen(req).read()
            if not os.path.exists(DIR):
                os.mkdir(DIR)
            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            print("...")
            filename = DIR + query + "+" + str(x) + ".jpg"
            print filename
            f = open(filename, 'wb')

            f.write(raw_img)
            f.close()
            x = int(x) + 1
            subprocess.Popen(
                "DISPLAY=:0 GSETTINGS_BACKEND=dconf /usr/bin/gsettings set org.gnome.desktop.background picture-uri file://{0}".format("/media/adi/Coding/git/Python/os/freshWall/images/coding+wallpapers+0.jpg"), shell=True)

            break
        except Exception as e:
            print "could not load : " + str(img)
            print e

# All you have to do is populate the query_list with names of search queiries .
scrapeGoogle("funny wallpapers")
