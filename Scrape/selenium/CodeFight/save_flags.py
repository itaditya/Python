import urllib2

src_file = open("flag_src.txt", "r")
# content = src_file.read()
sources = src_file.read().splitlines()
f = open("flags/MW.svg", 'wb')
header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

for source in sources:
    # name = source[source.rindex("/"):]
    name = source[-7:]
    print(name)
    try:
        # pass
        req = urllib2.Request(source, headers={'User-Agent': header})
        raw_img = urllib2.urlopen(req).read()
        f = open("flags" + name, 'wb')
        f.write(raw_img)
    finally:
        f.close()
