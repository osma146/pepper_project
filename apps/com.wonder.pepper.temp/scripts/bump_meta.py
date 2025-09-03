#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, uuid
import xml.etree.ElementTree as ET
import configparser

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
    # try direct finds
    for t in tags:
        el = root.find(t)
        if el is not None:
            return el
    # try namespace-agnostic (endswith)
    want = set([t.strip('/').split('/')[-1] for t in tags])
    for el in root.iter():
        if el.tag.split('}')[-1] in want:
            return el
    return None

# name → folder name
e_name = find1(['name', './package/name', './Name'])
if e_name is None:
    e_name = ET.SubElement(root, 'name')
e_name.text = APP_NAME

# vendor → literal text
e_vendor = find1(['vendor', './package/vendor', './Vendor'])
if e_vendor is None:
    e_vendor = ET.SubElement(root, 'vendor')
e_vendor.text = 'put name here'

# uuid/id → new UUID
e_uuid = find1(['uuid', 'id', './package/uuid', './Uuid', './Id'])
if e_uuid is None:
    e_uuid = ET.SubElement(root, 'uuid')
e_uuid.text = NEW_UUID

# backup before overwriting
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

with open(INI, 'rb') as r, open(INI + '.bak', 'wb') as b:
    b.write(r.read())

with open(INI, 'w') as f:
    cfg.write(f)

print("Done:")
print("  name    =", APP_NAME)
print("  vendor  = put name here")
print("  uuid    =", NEW_UUID)
