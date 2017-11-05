# -*- coding: utf-8 -*-

import json
import codecs
import os

fns = os.listdir('.')

emojis = {}

for fn in fns:
  if not fn.endswith('.json'): continue
  print fn
  txt = codecs.open(fn).read()
  obj = json.loads(txt)
  
  for item in obj['data']:
    print item['id'], item['tag'].encode('utf8'), item['entry'].encode('utf8')
    if item['tag'] not in emojis: 
      emojis[item['tag']] = []
    emojis[item['tag']].append(item['entry'])

print 'combined %d emojis' % len(emojis.keys())

# save

data = {'tag': emojis.keys(), 'emojis': emojis}
codecs.open('emojis.data', 'w', 'utf8').write(json.dumps(data))
print 'done!'