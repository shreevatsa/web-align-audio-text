import sys
import requests
import string
import re

template = string.Template('''
---
kind: "page"
layout: "sargapage"
ramayanaalignment: "$jsonpath"
ramayanaaudiourl: "$url"
---
'''.strip())

if __name__ == '__main__':
    json_filename = sys.stdin.readline().strip()
    suffix = '.json'
    assert json_filename.endswith(suffix), json_filename
    path = json_filename[:-len(suffix)]
    assert path.startswith('Kanda_'), path
    kanda_path = path[:len('Kanda_')+1]
    kanda_num = kanda_path[-1]
    m = re.match(kanda_path +'_([A-Z]{2,3})-([0-9][0-9][0-9])-.*.json', json_filename)
    sarga_num = m.group(2)
    url_prefix = 'https://archive.org/download/Ramayana-recitation-Sriram-harisItArAmamUrti-Ghanapaati-v2'
    url = f'{url_prefix}/{kanda_path}/{path}.mp3'
    print(url)
    # resp = requests.head(url, allow_redirects=True)
    # assert resp.status_code == 200 and int(resp.headers['Content-Length']) > 0, resp.headers
    out_filename = f'content/sarga/{kanda_num}.{sarga_num}.md'
    print(f'Writing to {out_filename}')
    with open(out_filename, 'w') as f:
        f.write(template.substitute(url=url, jsonpath=json_filename))
