import urllib2

# sources = ["Trainee", "Soldier", "Recruit", "Captain", "Warrior", "Ninja"]
sources = ["Soldier", "Recruit", "Captain", "Warrior", "Ninja"]
base_url = "https://codefights.com/user-icons/levels/"
f = open("badges/Trainee_1.svg", 'wb')
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

for source in sources:
    for i in xrange(1, 6):
        name = source + "_" + str(i)
        url = base_url + name + "_star.svg"
        print(name)
        try:
            req = urllib2.Request(url, headers={'User-Agent': header})
            raw_img = urllib2.urlopen(req).read()
            f = open("badges/" + name + ".svg", 'wb')
            f.write(raw_img)
        finally:
            f.close()
