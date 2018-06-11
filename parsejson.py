import urllib
import json
#url = http://py4e-data.dr-chuck.net/comments_53152.json
url = raw_input('Enter location: ')
jso = urllib.urlopen(url).read().decode()
print('...... Retrieving data from url ......')
js = json.loads(jso)
x = js["comments"]
sum = 0
count = 0
greatest = 0
for i in range(len(x)):
        y = x[i]["count"]
        sum = sum + y
        count = count + 1
        if i >= greatest:
                greatest = i
print('Total number of comments: %s')%(sum)
print('Number of users that commented: %s')%(count)
print('Most number of comments by a single user: %s')%(greatest)
