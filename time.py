#!/usr/bin/env python3.4
import datetime

now = datetime.datetime.now()

print ("Current Date using str\t",str(now))
print ("Current year %d \t" %now.year)
print ("Current strftime")
print (now.strftime("%Y-%m %H:%M"))

print (now.isoformat())
