import sys
import requests
import string
import re

template = string.Template('''
---
kind: "page"
layout: "ramepage"
alignmentjson: "$jsonpath"
alignmentaudio: "$url"
---
'''.strip())

if __name__ == '__main__':
    json_path = sys.stdin.readline().strip()
    # Remove data/audio_alignment/ from start.
    prefix = 'data/audio_alignment/'
    assert json_path.startswith(prefix)
    json_path = json_path[len(prefix):]
    # Remove .json at end of filename.
    suffix = '.json'
    assert json_path.endswith(suffix), json_path
    path = json_path[:-len(suffix)]
    # Find the Kanda path and number
    assert 'Kanda_' in path, path
    path = path[path.find('Kanda_'):]
    kanda_path = path[path.find('Kanda_'): path.find('Kanda_') + len('Kanda_') + 1]
    kanda_num = kanda_path[-1]
    m = re.match('ramayana/word_alignment/' + kanda_path + '_([A-Z]{2,3})-([0-9][0-9][0-9])-.*.json', json_path)
    sarga_num = m.group(2)
    url_prefix = 'https://archive.org/download/Ramayana-recitation-Sriram-harisItArAmamUrti-Ghanapaati-v2'
    url = f'{url_prefix}/{kanda_path}/{path}.mp3'
    print(url)
    # resp = requests.head(url, allow_redirects=True)
    # assert resp.status_code == 200 and int(resp.headers['Content-Length']) > 0, resp.headers
    out_filename = f'content/sarga/{kanda_num}.{sarga_num}.md'
    print(f'Writing to {out_filename}')
    with open(out_filename, 'w') as f:
        f.write(template.substitute(url=url, jsonpath=json_path))
