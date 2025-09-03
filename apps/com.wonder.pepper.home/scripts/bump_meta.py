#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, uuid
import xml.etree.ElementTree as ET
import configparser

# ── config you can change ──────────────────────────────────────────────────────
VENDOR_TEXT       = 'put name here'
DESC_TEXT         = 'put description here'
MAINTAINER_NAME   = 'your name'
MAINTAINER_EMAIL  = 'your@email'
ICON_PATH         = 'html/assets/image/put icon name here.png'
# ───────────────────────────────────────────────────────────────────────────────

# if no path is given, use parent folder of this script
if len(sys.argv) > 1:
    ROOT = sys.argv[1]
else:
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MANIFEST = os.path.join(ROOT, 'manifest.xml')
INI = os.path.join(ROOT, 'package.ini')
APP_NAME = os.path.basename(os.path.abspath(ROOT))
NEW_UUID = str(uuid.uuid4())

if not os.path.isfile(MANIFEST):
    raise SystemExit("manifest.xml not found at {}".format(MANIFEST))
if not os.path.isfile(INI):
    open(INI, 'a').close()

# ---- manifest.xml ----
tree = ET.parse(MANIFEST)
root = tree.getroot()

def find1(tags):
    # direct find
    for t in tags:
        el = root.find(t)
        if el is not None:
            return el
    # namespace-agnostic (match by localname)
    want = set([t.strip('/').split('/')[-1] for t in tags])
    for el in root.iter():
        if el.tag.split('}')[-1] in want:
            return el
    return None

def upsert_text(tag_candidates, default_tag, value):
    el = find1(tag_candidates)
    if el is None:
        el = ET.SubElement(root, default_tag)
    el.text = value

# name → folder name
upsert_text(['name','./package/name','./Name'], 'name', APP_NAME)

# vendor
upsert_text(['vendor','./package/vendor','./Vendor'], 'vendor', VENDOR_TEXT)

# uuid/id
e_uuid = find1(['uuid','id','./package/uuid','./Uuid','./Id'])
if e_uuid is None:
    e_uuid = ET.SubElement(root, 'uuid')
e_uuid.text = NEW_UUID

# description
upsert_text(['description','./package/description','./Description'], 'description', DESC_TEXT)

# maintainer (name)
upsert_text(['maintainer','./package/maintainer','./Maintainer'], 'maintainer', MAINTAINER_NAME)

# maintainer email
upsert_text(['maintainer_email','maintainerEmail','./package/maintainer_email','./package/maintainerEmail','./MaintainerEmail'],
            'maintainer_email', MAINTAINER_EMAIL)

# backup then write
with open(MANIFEST, 'rb') as r, open(MANIFEST + '.bak', 'wb') as b:
    b.write(r.read())
tree.write(MANIFEST, encoding='utf-8', xml_declaration=True)

# ---- package.ini ----
cfg = configparser.ConfigParser()
try:
    cfg.read(INI, encoding='utf-8')  # py3
except TypeError:
    cfg.read(INI)  # py2

if not cfg.has_section('package'):
    cfg.add_section('package')

cfg.set('package', 'name', APP_NAME)
cfg.set('package', 'uuid', NEW_UUID)
cfg.set('package', 'description', DESC_TEXT)
cfg.set('package', 'maintainer', MAINTAINER_NAME)
cfg.set('package', 'maintainer_email', MAINTAINER_EMAIL)
cfg.set('package', 'vendor', VENDOR_TEXT)
cfg.set('package', 'icon', ICON_PATH)

# backup then write
with open(INI, 'rb') as r, open(INI + '.bak', 'wb') as b:
    b.write(r.read())
with open(INI, 'w') as f:
    cfg.write(f)

print("Done:")
print("  name        =", APP_NAME)
print("  vendor      =", VENDOR_TEXT)
print("  uuid        =", NEW_UUID)
print("  description =", DESC_TEXT)
print("  maintainer  =", MAINTAINER_NAME, "<"+MAINTAINER_EMAIL+">")
print("  icon        =", ICON_PATH)
