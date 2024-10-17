import subprocess

def detect_package_manager():
    """Detect the system's package manager."""
    package_managers = {
        'apt': ['sudo', 'apt', 'install', '-y'],
        'dnf': ['sudo', 'dnf', 'install', '-y'],
        'pacman': ['sudo', 'pacman', '-S', '--noconfirm'],
        'zypper': ['sudo', 'zypper', 'install', '-y']
    }

    for manager in package_managers:
        if subprocess.run(['which', manager], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0:
            return manager, package_managers[manager]

    return None, "No supported package manager detected on this system."

def collect_necessary_packages(manager):
    """Return the list of necessary packages for the detected package manager."""
    # Define the necessary packages for each package manager
    package_map = {
    'apt': ['gnome-tweaks', 'gnome-shell-extensions', 'dconf-cli'],
    'dnf': ['gnome-tweaks', 'gnome-shell-extension-user-theme'],
    'pacman': ['gnome-tweaks', 'gnome-shell-extensions'],
    'zypper': ['gnome-tweaks', 'gnome-shell-extensions']
    }

    if manager not in package_map:
        raise ValueError(f"Package manager '{manager}' is not supported.")

    # Return the packages needed for the specific package manager
    return package_map[manager]

