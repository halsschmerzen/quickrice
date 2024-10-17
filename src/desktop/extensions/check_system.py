import os, subprocess

def return_distro():
    distro_info = {}

    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release") as f:
            for line in f:
                key, _, value = line.partition("=")
                distro_info[key.strip()] = value.strip().strip('"')
    else:
        print('Distribution could not be determined!')
        return None
    return distro_info