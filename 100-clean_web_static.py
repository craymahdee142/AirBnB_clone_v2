#!/usr/bin/python3
# Fabric file delete out-of-date archives

import os
from fabric.api import *

env.hosts = ['17.206.20.255', '34.73.75.125']


def do_clean(number=0):
    """Delete out of date archives
    Args:
        number (int): number of archives to keep
        if number is 0 r 1 keep only most recent
        if number is 2, keep the most and second most recent
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives  = [a for a archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
