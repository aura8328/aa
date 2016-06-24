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
exit()


"""
for k, v in sparam.items():
    # print 'v: '+ k + str(v)
    for idx, child in enumerate(soup.body.children):
        if idx != int(v):
            break
        print child

def find_child_from_idx(root_obj, child_name, idx):
    tmp_obj = root_obj.find_next_sibling(child_name)
    if idx == 0:
        return tmp_obj
    for i in range(0,idx):
        tmp_obj = tmp_obj.find_next_sibling(child_name)
    return tmp_obj

print 'get_ch'
a = find_child_from_idx(soup, 'html', 0)
print a
b = find_child_from_idx(a, 'body', 0)
c = find_child_from_idx(b, 'a', 0)
print c


for idx, v in enumerate(sparam.items()):
    if idx + 1 > len(sparam):
        print 'return'
    else:
        get_child(k, v)
    print idx + 1
    print len(sparam)


for a in soup.findAll('html'):
    print type(a)

print soup.find('html').find('body').find('p').find_next_sibling('p')
"""
