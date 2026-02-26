#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of the AirBnB Clone repository.
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Packs the web_static folder into a compressed .tgz archive.
    
    Returns:
        The path to the generated archive if successful, otherwise None.
    """
    # 1. Create the 'versions' folder if it doesn't already exist
    # The -p flag (parents) ensures it doesn't throw an error if the folder is already there
    local("mkdir -p versions")

    # 2. Grab the current date and time
    now = datetime.now()
    
    # 3. Format the time exactly as requested: <year><month><day><hour><minute><second>
    # %Y = Year, %m = Month, %d = Day, %H = Hour, %M = Minute, %S = Second
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # 4. Construct the exact file path and name
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # 5. Execute the local command to compress the files
    print("Packing web_static to {}".format(archive_path))
    result = local("tar -cvzf {} web_static".format(archive_path))

    # 6. Check if the command was successful and return the path
    if result.succeeded:
        return archive_path
    else:
        return None
