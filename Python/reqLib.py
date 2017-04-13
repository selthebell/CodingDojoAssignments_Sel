import requests
r = requests.get('https://api.github.com/events')
print type(r)
#print dir(r)
a=r.json();
try:
    for i in a:
        for j in i:
            print i[j]
except:
    print "error"
