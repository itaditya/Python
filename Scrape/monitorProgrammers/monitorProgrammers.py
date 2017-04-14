import requests
import bs4
import json
from tabulate import tabulate
from datetime import datetime
from dateutil import relativedelta

print "\n"+"-"*10+"-"*10
db_file = 'usernames.json'
table = []
print " Hold On ! Loading the data\n \n [",
with open(db_file) as data_file:
    data = json.load(data_file)
    last_check = datetime.strptime(data["last_check"], '%Y-%m-%d %H:%M:%S')
    # last_check = str(data["last_check"])
    user_data = data["users"]
    codechef_root_url = 'https://www.codechef.com/users/'
    hackerrank_root_url = 'https://www.hackerrank.com/users/'
    # print "Name \tTotal Solved \tNew Attempts"
    for user in user_data:
        index_url = codechef_root_url + user["codechef_id"]
        response = requests.get(index_url)
        soup = bs4.BeautifulSoup(response.text ,"html.parser")
        prob_header = soup.select('.problems-solved .content h5')
        print "=",
        prob_fully = prob_header[0].text
        prob_partially = prob_header[1].text
        user_curr_fully = int(prob_fully[prob_fully.find("(")+1:prob_fully.find(")")])
        user_curr_partially = int(prob_partially[prob_partially.find("(")+1:prob_partially.find(")")])
        user_curr_total = user_curr_fully + user_curr_partially
        user_new_fully = user_curr_fully - int(user["last_fully"])
        user_new_partially = user_curr_partially - int(user["last_partially"])
        user_new_total = user_curr_total - int(user["last_total"])
        user["last_fully"] = user_curr_fully
        user["last_partially"] = user_curr_partially
        user["last_total"] = user_curr_total
        table.append([user["name"],user_curr_total,user_new_total])
print "]\n\n"
cur_date = datetime.now()
rd = relativedelta.relativedelta(cur_date, last_check)
time_diff = "{} months, {} days )".format(rd.months, rd.days)
print tabulate(table, headers=["Name","Total Solved","New Attempts ( after "+time_diff])
with open(db_file,'w') as data_file:
    data["last_check"] = cur_date.strftime("%Y-%m-%d %H:%M:%S")
    json.dump(data, data_file)

print "\n"+"-"*10+"-"*10

