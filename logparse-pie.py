import matplotlib.pyplot as plt
f = open('/var/log/yum.log')
I = {}
c = 0
d = 0
e = 0
for i in f.readlines():
    # print(i.split(' ')[3])
    if 'Installed' in i.split(' ')[3]:
        I['Installed'] = c
        c = c + 1
    elif 'Updated' in i.split(' ')[3]:
        I['Updated'] = d
        d = d + 1
    elif 'Erased' in i.split(' ')[3]:
        I['Erased'] = e
        e = e + 1
labels = 'Installed','Updated','Erased'
sizes = [I['Installed'],I['Updated'],I['Erased']]
print(sizes)
fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.pie(sizes, labels=labels, explode=None, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
