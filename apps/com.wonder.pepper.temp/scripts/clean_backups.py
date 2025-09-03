#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

# if path is given, use it; else go up one level (parent of script/)
if len(sys.argv) > 1:
    ROOT = sys.argv[1]
else:
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

deleted = 0
for dirpath, dirnames, filenames in os.walk(ROOT):
    for fname in filenames:
        if fname.endswith('.bak'):
            fpath = os.path.join(dirpath, fname)
            try:
                os.remove(fpath)
                print("Deleted:", fpath)
                deleted += 1
            except Exception as e:
                print("Failed:", fpath, "->", e)

print("Done. Deleted {} backup files.".format(deleted))
