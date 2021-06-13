import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1179849.json')
data = address.read().decode()
js = json.loads(data)
#print(len(js['comments']))
i = 0
soma = 0
while i < 50:
    print(js['comments'][i]['count'])
    soma += int(js['comments'][i]['count'])
    i += 1
print(soma)
