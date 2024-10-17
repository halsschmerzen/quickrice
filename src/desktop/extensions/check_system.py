import os, subprocess

def check_package_manager():

    package_managers = {
        'apt' : 'apt-get',
        'pacman' : 'pacman',
        'dnf' : 'dnf'
    }

    for manager, command in package_managers.items():
        try:
            subprocess.run([command, '--version'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            return manager
        except FileNotFoundError:
            continue
    
    return None

