#!/usr/bin/env python3

import os
import sys

tmpl_url = (
    "https://raw.githubusercontent.com/davidspies/snapshots/master/"
    + "dspies.hsfiles"
    )
resolver = (
    'https://raw.githubusercontent.com/davidspies/snapshots/master/' +
    'dspies-snapshot-2.yaml'
    )

def main(loc, *args):
    os.execvp("stack", ("stack", "new", loc, tmpl_url, '--resolver=' + resolver) + args)


if __name__ == '__main__':
    main(*sys.argv[1:])
