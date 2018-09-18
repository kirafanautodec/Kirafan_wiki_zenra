#!/usr/bin/env python3
import os
import sys
import time
import re
import struct
import json
import glob
import yaml
import datetime

cwd = os.path.dirname(os.path.abspath(__file__))
srcdir = cwd + "/../articles/"
distdir = cwd + "/../dist/"
os.makedirs(distdir, exist_ok=True)
category_meta = yaml.load(open(srcdir + "categories.yaml"))
srcfiles = glob.glob(srcdir + "**/**.md", recursive=True)
metalines = slice(1, 4)

categories = []
artitles = {}
artitles_list = []

count = 0
for filepath in srcfiles:
    filename = filepath[len(srcdir):]
    mtime = os.stat(filepath).st_mtime
    category = filename.split('/')[0]
    if not category in categories:
        categories.append(category)
        artitles[category] = []
  
    file = open(filepath)
    mdcontent = file.read().split('\n')[metalines]
    metayml = "\n".join(mdcontent)
    meta = yaml.load(metayml)

    meta["id"] = count
    meta["filepath"] = filename
    meta["edittime"] = datetime.datetime.fromtimestamp(int(mtime))

    artitles[category].append(meta)
    artitles_list.append(meta)

    count += 1

with open(distdir + "meta.json", "wb") as of:
    string = json.dumps({
        "categories": category_meta,
        "artitles" : artitles,
        "artitles_list": artitles_list
    }, ensure_ascii=False, indent=2, default=str)
    of.write(string.encode('utf-8'))

print(category_meta)
print(artitles)
    
  