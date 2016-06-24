import urllib
import bs4


html= """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<div><span><a href=http://naver.com>naver.com</a></span></div>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
input = 'html.body_1.p.a_2'


sparam = []
for sub in input.split('.'):
    try:
        sparam.append((sub.split('_')[0], sub.split('_')[1]))
    except IndexError as e:
        sparam.append((sub.split('_')[0], '0'))


print sparam


soup = bs4.BeautifulSoup(html, 'html.parser')

tmp_css = ""
for k, v in sparam:
    if tmp_css != "":
        tmp_css = tmp_css + ' > '
    tmp_css = tmp_css + str(k)
    if v == '0':
        continue
    tmp_css = tmp_css + ':nth-of-type('+ str(v) + ')'
    print tmp_css

print soup.select(tmp_css)
