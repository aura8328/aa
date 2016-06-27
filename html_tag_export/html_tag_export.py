import urllib
import platform
import os
import sys
import bs4

PLATFORM = platform.system()
if PLATFORM == 'Windows':
    DIR_TOC = '\\'
elif PLATFORM == 'Linux':
    DIR_TOC = '/'
else:
    DIR_TOC = '/'



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
input = 'html.body_1'

def trans_param(input):
    sparam = []
    for sub in input.split('.'):
        try:
            sparam.append((sub.split('_')[0], sub.split('_')[1]))
        except IndexError as e:
            sparam.append((sub.split('_')[0], '0'))
    # print sparam
    return sparam


def find_html_from_tag(input, bsObj):
    sparam = trans_param(input)
    tmp_css = ""
    for k, v in sparam:
        if tmp_css != "":
            tmp_css = tmp_css + ' > '
        tmp_css = tmp_css + str(k)
        if v == '0':
            continue
        tmp_css = tmp_css + ':nth-of-type('+ str(v) + ')'
        # print tmp_css

    return bsObj.select(tmp_css)

"""

Input Args 1 - Target Directory Root Path

"""
def main(argv):
    if len(argv) != 2:
        print('argv err')
        exit(-1)


    input = argv[0]
    root_dir = argv[1]
    result_root_dir = root_dir + '_' + input

    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            f_path = os.path.join(root, filename)

            ## Result Directory Path Gen and Directory Create
            t_path = f_path.split(root_dir)[-1]
            result_dir = result_root_dir + t_path
            try:
                os.makedirs(os.path.dirname(result_dir))
            except Exception as e:
                # print("makedirs : {}".format(e))
                pass

            if os.path.splitext(f_path)[1] not in ['.html', '.htm']:
                # print str(f_path) + ': is not html file.'
                continue
            with open(f_path, 'r') as f:
                html = f.read()

            soup = bs4.BeautifulSoup(html, 'html.parser')
            try:
                result = find_html_from_tag(input, soup)[0]
            except IndexError as e:
                pass

            with open(result_dir, 'w') as f:
                f.write(result.prettify().encode('utf-8'))

            # print result.prettify()


if __name__ == "__main__":
   main(sys.argv[1:])