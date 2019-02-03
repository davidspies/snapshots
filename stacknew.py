#!/usr/bin/env python3

import os
import sys

tmpl_url = (
    "https://raw.githubusercontent.com/davidspies/snapshots/master/"
    + "dspies.hsfiles"
    )


def main(loc, *args):
    os.execvp("stack", ("stack", "new", loc, tmpl_url) + args)


if __name__ == '__main__':
    main(*sys.argv[1:])
