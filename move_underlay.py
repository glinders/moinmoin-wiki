#!/usr/bin/python

from glob import glob
from os import renames
from os.path import join, dirname, basename, normpath, abspath
import shutil

def pages_by_lang(pagesdir):
    """Returns a dictionary of #language to page path."""
    pages = {}
    for path in glob(join(pagesdir,'*','revisions', '00000001')):
        pages.setdefault(scan_for_lang(path), 
            []).append(basename(dirname(dirname(normpath(path)))))
    return pages

def scan_for_lang(path):
    """Returns #language from path or 'None' if #language not found."""
    for line in file(path):
        # We assume no language declaration can occur after a blank line
        if line[0] != '#':
            break
        if line.startswith('#language '):
            return line.split()[1]
    return None

def move_unwanted(pagesdir, unwanteddir, wantedlangs=[None, 'en']):
    pages = pages_by_lang(pagesdir)
    for lang, paths in pages.iteritems():
        if lang not in wantedlangs:
            for pagedir in paths:
                shutil.move(join(pagesdir, pagedir), join(unwanteddir, pagedir))

if __name__ == '__main__':
    move_unwanted(abspath('./underlay/pages'), abspath('./unwanted/pages'))
