#!/usr/bin/python3
# Fabric script that generates a .tgz archive from the contents of the
# web_static folder of your AirBnB Clone repo, using the function do_pack

import os
import tarfile
import datetime
from fabric.api import *

def do_pack():

    result = run("-d /versions")

    if result.succeeded is False:
        run("mkdir /versions")

    time = datetime.datetime.now()
    name = "web_static_" + time.strftime("%Y%m%d%H%M%S")
    path = "./web_static"

    with tarfile.open(name, "x") as tar_handle:
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    tar_handle.add(os.path.join(root, file))
            return tar_handle

        except:
            return None
