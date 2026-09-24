import re, json
html = open('index.html', encoding='utf-8').read()
scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
for i, s in enumerate(scripts):
    try:
        json.loads(s)
        print(f'script {i}: OK')
    except Exception as e:
        print(f'script {i}: ERROR {e}')
