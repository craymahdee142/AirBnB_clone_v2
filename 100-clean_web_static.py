#!/usr/bin/python3
# Fabric file delete out-of-date archives

import os
from fabric.api import env, lcd, local, run, cd

env.hosts = ['54.157.147.218', '3.85.41.177']
evn.user = 'ubuntu'


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
        archives = [a for a in archives if "web_static_" in a]
        for i in range(number):
            archives.pop()
        [run("rm -rf ./{}".format(a)) for a in archives]
