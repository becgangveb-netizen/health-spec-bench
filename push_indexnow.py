import json, sys, urllib.request

HOST = sys.argv[1] if len(sys.argv) > 1 else 'example.github.io'
KEY = 'healthspecbench'
URLS = ['https://%s/health-spec-bench/' % HOST, 'https://%s/health-spec-bench/c1.html' % HOST]
body = json.dumps({'host': HOST, 'key': KEY, 'keyLocation': 'https://%s/%s.txt' % (HOST, KEY), 'urlList': URLS}).encode()
req = urllib.request.Request('https://api.indexnow.org/indexnow', data=body, headers={'Content-Type': 'application/json; charset=utf-8'})
print(urllib.request.urlopen(req, timeout=10).status)
