import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1179848.xml')
#xmldoc = ETaddress)
data = address.read()
#print(data.decode())
root = ET.fromstring(data)
soma = 0
for comment in root.iter('comment'):
    #print(comment.find('name').text)
    #print(comment.find('count').text)
    soma += int(comment.find('count').text)
print(soma)








"""address = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_42.xml')
#xmldoc = ETaddress)
data = address.read()
for i in data:
    print(i)"""


