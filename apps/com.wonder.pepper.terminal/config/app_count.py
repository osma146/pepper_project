#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json

def derive_prefix(app_folder_name):
    parts = app_folder_name.split('.')
    # Use first 3 labels if available (e.g., com.wonder.pepper.)
    if len(parts) >= 3:
        base = '.'.join(parts[:3]) + '.'
    elif len(parts) == 2:
        base = '.'.join(parts) + '.'
    else:
        base = parts[0] + '.'
    return base

def main():
    here = os.path.abspath(os.path.dirname(__file__))      # ...\com.wonder.pepper.home\config
    app_root = os.path.abspath(os.path.join(here, os.pardir))   # ...\com.wonder.pepper.home
    container = os.path.dirname(app_root)                  # parent dir containing all apps
    cfg_file = os.path.join(here, 'app_local.json')        # JSON lives in this app's config

    app_folder_name = os.path.basename(app_root)
    prefix = derive_prefix(app_folder_name)

    # Count sibling folders in container that start with derived prefix
    try:
        names = os.listdir(container)
    except OSError:
        print('Container not found:', container)
        return

    count = 0
    for name in names:
        if name.startswith(prefix):
            p = os.path.join(container, name)
            if os.path.isdir(p):
                count += 1

    # Merge into existing JSON
    data = {}
    if os.path.isfile(cfg_file):
        try:
            with open(cfg_file, 'r') as f:
                data = json.load(f)
        except Exception:
            data = {}

    ns = data.get('namespace_counts', {})
    ns[prefix] = count
    data['namespace_counts'] = ns
    data['apps_container'] = container
    data['app_root'] = app_root
    data['derived_prefix'] = prefix

    # Write back
    with open(cfg_file, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)

    print('Prefix:', prefix)
    print('Count:', count)
    print('Container:', container)
    print('Updated:', cfg_file)

if __name__ == '__main__':
    main()
