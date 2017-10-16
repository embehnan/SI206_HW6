from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter -')
count= int(input ('Enter count:'))
position= int(input('Enter position:'))



for x in range(int(count)):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags=soup('a')
    num=0
    for tag in tags:
        num +=1
        if num ==int(position):
            url =tag.get('href')
            if x==int(count)-1:
                print (tag.contents[0])
