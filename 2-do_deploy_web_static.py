#!/usr/bin/python3
"""
A Fabric script that distributes an archive to your web servers.
"""
from fabric.api import env, put, run
import os

# Define the servers to deploy to
env.hosts = ['52.91.210.233', '54.237.133.112']
# Define the user
env.user = 'ubuntu'

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.
    
    Args:
        archive_path (str): The path to the archive to deploy.
        
    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    # 1. Return False if the file at the path doesn't exist
    if not os.path.exists(archive_path):
        return False

    try:
        # Extract the file name (e.g., 'web_static_20170315003959.tgz')
        file_name = archive_path.split('/')[-1]
        
        # Extract the file name without the extension (e.g., 'web_static_20170315003959')
        name_no_ext = file_name.split('.')[0]
        
        # Define the exact release path on the server
        release_path = "/data/web_static/releases/{}/".format(name_no_ext)

        # 2. Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp/{}".format(file_name))

        # 3. Create the new release directory on the server
        run("mkdir -p {}".format(release_path))

        # 4. Uncompress the archive to the new folder
        run("tar -xzf /tmp/{} -C {}".format(file_name, release_path))

        # 5. Delete the uploaded archive from the web server's /tmp/ folder
        run("rm /tmp/{}".format(file_name))

        # 6. The "Russian Doll" fix: Move the files out of the inner web_static folder
        run("mv {}web_static/* {}".format(release_path, release_path))

        # 7. Delete the empty inner web_static folder
        run("rm -rf {}web_static".format(release_path))

        # 8. Delete the old symbolic link
        run("rm -rf /data/web_static/current")

        # 9. Create the new symbolic link linked to the new version
        run("ln -s {} /data/web_static/current".format(release_path))

        print("New version deployed!")
        return True

    except Exception:
        # If anything goes wrong during the try block, return False
        return False
