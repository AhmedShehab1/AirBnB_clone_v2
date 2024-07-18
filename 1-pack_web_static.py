#!/usr/bin/python3

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Packing web_static to versions/web_static_20170314233357.tgz
    """
    local("mkdir -p versions")
    archive_name = "/versions/web_static_{}.tgz"
    .format(datetime.now().strftime("%Y%m%d%H%M%S"))
    local("tar -czvf {} web_static".format(archive_name))
