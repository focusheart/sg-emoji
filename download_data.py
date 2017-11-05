import requests
import codecs
import os
import time
import json

url = 'http://pinyin.sogou.com/dict/ywz/ajax/make_list.php'

def download(tag_id, tag_page, tag_type="tag"):
  fn = 'data-%s-%s-%s.json' % (tag_type, tag_id, tag_page)
  if os.path.exists(fn):
    print '* exists %s' % fn
    return

  form = {
    'tag_id': tag_id,
    'type': tag_type,
    'page': tag_page
  }

  req = requests.post(url, data=form)
  txt = req.text
  codecs.open(fn, 'w', 'utf-8').write(txt)

  print '* got %s' % fn
  
def manuel_mode():
  tag_id = raw_input('Tag ID: ')
  tag_page = raw_input('Tage Page: ')

  download(tag_id, tag_page)

def auto_mode():
  for i in range(1, 24):
    download(i, 1)
    time.sleep(3)

def auto_all_mode_by_pageone():
  for i in range(1, 24):
    # load page 1 info
    fn = 'data-%s-%s-%s.json' % ('tag', i, 1)
    obj = json.loads(codecs.open(fn, 'r', 'utf-8').read())
    num_pages = obj['page']
    if num_pages <= 1: continue

    # download pages from page 2
    for j in range(2, num_pages+1):
      download(i, j)
      time.sleep(3)

auto_all_mode_by_pageone()