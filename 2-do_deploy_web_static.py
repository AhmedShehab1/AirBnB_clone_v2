#!/usr/bin/python3
import os
from fabric.api import *


env.hosts = ["web-01.ahmedshehab.tech",
             "web-02.ahmedshehab.tech"]


def log(msg):
    """Showing informative msgs"""
    print(f"[INFO]: {msg}")


def run_command(command):
    """handles command execution logic"""
    result = run(command)
    if result.failed:
        log(f"Command failed: {command}")
        return False
    return True


def do_deploy(archive_path):
    """Deploying archive to both web servers"""
    if not os.path.exists(archive_path):
        return (False)
    log("Uploading archive to /tmp/")
    if not put(archive_path, "/tmp/"):
        return (False)
    log("removing old symbolic_link")
    if not run_command("rm -rf /data/web_static/current"):
        return (False)
    new_dir = archive_path.split("/")[1].split(".")[0]
    log("Creating new directory to extract archive in")
    if not run_command(f"mkdir -p /data/web_static/releases/{new_dir}"):
        return (False)
    log("extracting archive to new dir")
    if not run_command(f"tar -xzf /tmp/{new_dir}.tgz -C\
 /data/web_static/releases/{new_dir}"):
        return (False)
    if not run_command(f"mv /data/web_static/releases/{new_dir}/web_static/*\
 /data/web_static/releases/{new_dir}"):
        return (False)
    if not run_command(f"rm -rf /data/web_static/releases/{new_dir}\
/web_static"):
        return (False)
    log("Removing archive from remote...")
    if not run_command("rm -rf /tmp/*.tgz"):
        return (False)
    log("creating new symlink")
    if not run_command(f"ln -s /data/web_static/releases/{new_dir}\
 /data/web_static/current"):
        return (False)
    return (True)
