#!/usr/bin/env python3

import os
import subprocess
import sys


def subcall(args):
    res = subprocess.run(args)
    res.check_returncode()


def subrun(args):
    res = subprocess.run(args, stdout=subprocess.PIPE)
    res.check_returncode()
    return res.stdout.decode().strip()


def main(opt, *args):
    database = os.path.join(
        subrun(["stack", "path", "--local-hoogle-root"]), "database.foo"
    )
    if opt == "setup":
        subcall(["stack", "haddock", "--test", "--no-run-tests"])
        localDocRoot = subrun(["stack", "path", "--local-doc-root"])
        snapshotDoc = subrun(["stack", "path", "--snapshot-doc-root"])
        subcall(
            [
                "stack",
                "exec",
                "--",
                "hoogle",
                "generate",
                "--local=" + localDocRoot,
                "--local=" + snapshotDoc,
                "--database=" + database,
            ]
            + list(args)
        )
    elif opt == "server":
        subcall(["hoogle", "server", "--local", "--database=" + database] + list(args))
    else:
        raise Exception("Unknown argument: " + opt)


if __name__ == "__main__":
    main(*sys.argv[1:])

# Based on code by @gittywithexcitement :
# https://github.com/commercialhaskell/stack/issues/5228#issuecomment-629738842
