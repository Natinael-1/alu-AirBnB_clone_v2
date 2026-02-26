#!/usr/bin/python3
"""
A Fabric script that creates and distributes an archive to web servers.
"""
from fabric.api import env, local, put, run
from datetime import datetime
import os

# Define your specific remote web servers
env.hosts = ['52.91.210.233', '54.237.133.112']
env.user = 'ubuntu'

def do_pack():
    """
    Packs the web_static folder into a compressed .tgz archive.
    """
    local("mkdir -p versions")
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    print("Packing web_static to {}".format(archive_path))
    result = local("tar -cvzf {} web_static".format(archive_path))

    if result.succeeded:
        return archive_path
    else:
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        name_no_ext = file_name.split('.')[0]
        release_path = "/data/web_static/releases/{}/".format(name_no_ext)

        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(release_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(release_path, release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True

    except Exception:
        return False

def deploy():
    """
    Creates and distributes an archive to the web servers.
    This acts as the master orchestrator function.
    """
    # 1. Call do_pack and store the path
    archive_path = do_pack()

    # 2. Return False if no archive has been created
    if archive_path is None:
        return False

    # 3. Call do_deploy using the new path and return its result
    return do_deploy(archive_path)
