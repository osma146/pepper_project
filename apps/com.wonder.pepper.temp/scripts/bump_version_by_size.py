#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import xml.etree.ElementTree as ET

# Py2/3 configparser
try:
    import configparser
except ImportError:
    import ConfigParser as configparser  # Py2 (Pepper)

# --------- locate app root & files ----------
if len(sys.argv) >= 2:
    ROOT = os.path.abspath(sys.argv[1])
else:
    # parent of script/ (the entire app folder)
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MANIFEST = os.path.join(ROOT, 'manifest.xml')
INI      = os.path.join(ROOT, 'package.ini')

# --------- helpers ----------
EXCLUDED_DIRS  = {'.git', '__pycache__', 'node_modules', 'script'}
EXCLUDED_FILES = {'.DS_Store'}
EXCLUDED_ENDS  = ('.bak',)

def dir_total_bytes(path):
    total = 0
    for dp, dns, fns in os.walk(path):
        # skip excluded dirs
        dns[:] = [d for d in dns if d not in EXCLUDED_DIRS]
        for fn in fns:
            if fn in EXCLUDED_FILES or fn.endswith(EXCLUDED_ENDS):
                continue
            fp = os.path.join(dp, fn)
            try:
                if os.path.islink(fp):
                    continue
                total += os.path.getsize(fp)
            except Exception:
                pass
    return total

def parse_semver(s):
    try:
        parts = [int(x) for x in str(s).strip().split('.')]
        while len(parts) < 3: parts.append(0)
        return parts[:3]
    except Exception:
        return [0,0,0]

def semver_str(v):
    return '%d.%d.%d' % (v[0], v[1], v[2])

def version_max(v1, v2):
    return max(v1, v2)

def backup_file(path):
    if os.path.exists(path):
        with open(path, 'rb') as r, open(path + '.bak', 'wb') as b:
            b.write(r.read())

def upsert_xml_text(root, tag_candidates, default_tag, value):
    for t in tag_candidates:
        el = root.find(t)
        if el is not None:
            el.text = value
            return el
    want = set([t.strip('/').split('/')[-1] for t in tag_candidates])
    for el in root.iter():
        if el.tag.split('}')[-1] in want:
            el.text = value
            return el
    el = ET.SubElement(root, default_tag)
    el.text = value
    return el

# --------- load INI ----------
cfg = configparser.ConfigParser()
try:
    cfg.read(INI, encoding='utf-8')
except TypeError:
    cfg.read(INI)

if not cfg.has_section('package'):
    cfg.add_section('package')

# previous size: prefer new key 'tree_size', fallback to old 'main_size'
prev_size = None
if cfg.has_option('package', 'tree_size'):
    try: prev_size = int(cfg.get('package', 'tree_size'))
    except Exception: prev_size = None
elif cfg.has_option('package', 'main_size'):
    try: prev_size = int(cfg.get('package', 'main_size'))
    except Exception: prev_size = None

# current size of ENTIRE ROOT (minus exclusions)
curr_size = dir_total_bytes(ROOT)

# versions
if not os.path.isfile(MANIFEST):
    raise SystemExit("manifest.xml not found at {}".format(MANIFEST))
tree = ET.parse(MANIFEST)
root = tree.getroot()

ini_ver_str = cfg.get('package', 'version') if cfg.has_option('package', 'version') else '0.0.0'
ini_ver = parse_semver(ini_ver_str)

def get_xml_version(root):
    for t in ['version','./package/version','./Version']:
        el = root.find(t)
        if el is not None and (el.text or '').strip():
            return (el, parse_semver(el.text.strip()))
    for el in root.iter():
        if el.tag.split('}')[-1].lower() == 'version' and (el.text or '').strip():
            return (el, parse_semver(el.text.strip()))
    return (None, [0,0,0])

xml_ver_el, xml_ver = get_xml_version(root)
base_ver = version_max(ini_ver, xml_ver)

# compute bump
if prev_size is None:
    new_ver = base_ver[:]
    note = "initialized (no bump)"
else:
    if prev_size == 0:
        change_ratio = 1.0 if curr_size > 0 else 0.0
    else:
        change_ratio = abs(curr_size - prev_size) / float(prev_size)

    new_ver = base_ver[:]
    if change_ratio == 0.0:
        note = "no change"
    elif change_ratio < 0.05:
        new_ver[2] += 1
        note = "PATCH +1 (<5%)"
    elif change_ratio < 0.20:
        new_ver[1] += 1; new_ver[2] = 0
        note = "MINOR +1 (5–20%)"
    else:
        new_ver[0] += 1; new_ver[1] = 0; new_ver[2] = 0
        note = "MAJOR +1 (>=20%)"

# write back INI
cfg.set('package', 'version', semver_str(new_ver))
cfg.set('package', 'tree_size', str(curr_size))   # new canonical key
# keep legacy keys for compatibility (optional)
cfg.set('package', 'main', '.')                   # represents whole root
cfg.set('package', 'main_size', str(curr_size))   # mirrors tree_size

backup_file(INI)
with open(INI, 'w') as f:
    cfg.write(f)

# write back XML
upsert_xml_text(root, ['version','./package/version','./Version'], 'version', semver_str(new_ver))
backup_file(MANIFEST)
tree.write(MANIFEST, encoding='utf-8', xml_declaration=True)

print("Scope:      ENTIRE APP FOLDER =", ROOT)
print("Prev size:  {}".format(prev_size if prev_size is not None else "(none)"))
print("Curr size:  {}".format(curr_size))
if prev_size is None:
    print("Change:     (first run)")
else:
    pct = 0.0 if prev_size in (None,0) else (abs(curr_size - prev_size) * 100.0 / float(prev_size))
    print("Change:     {:+d} bytes ({:.2f}%)".format(curr_size - (prev_size or 0), pct))
print("Version:     {}  →  {}  [{}]".format(semver_str(base_ver), semver_str(new_ver), note))
print("Updated:     package.ini [package].version/tree_size (and legacy main/main_size)")
print("Updated:     manifest.xml <version>")
