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
import hashlib
import shutil

cwd = os.path.dirname(os.path.abspath(__file__))
srcdir = cwd + "/../articles/"
distdir = cwd + "/../dist/"
shutil.rmtree(distdir, ignore_errors=True)
shutil.copytree(srcdir, distdir)
category_meta = yaml.load(open(srcdir + "categories.yaml", "r", encoding="utf-8"))
srcfiles = glob.glob(srcdir + "**/**.md", recursive=True)
metalines = slice(1, 4)

categories = []
artitles = {}
artitles_list = {}

for filepath in srcfiles:
    filename = filepath[len(srcdir):]
    mtime = os.stat(filepath).st_mtime
    category = filename.split('/')[0]
    if not category in categories:
        categories.append(category)
        artitles[category] = []
  
    file = open(filepath, "r", encoding="utf-8")
    mdcontent = file.read().split('\n')[metalines]
    metayml = "\n".join(mdcontent)
    meta = yaml.load(metayml)

    md5id = hashlib.md5(filepath.encode('utf-8')).hexdigest()[:16]
    #meta["id"] = md5id
    meta["filepath"] = filename
    meta["edittime"] = datetime.datetime.fromtimestamp(int(mtime))

    artitles[category].append(md5id)
    artitles_list[md5id] = meta

with open(distdir + "meta.json", "wb") as of:
    string = json.dumps({
        "categories": category_meta,
        "artitles" : artitles,
        "artitles_list": artitles_list
    }, ensure_ascii=False, indent=2, default=str)
    of.write(string.encode('utf-8'))

