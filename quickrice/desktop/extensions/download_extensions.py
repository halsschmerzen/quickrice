from quickrice.desktop.extensions.check_system import detect_package_manager
import subprocess

def check_package_installed(package, manager):
    """Check if a package is installed based on the detected package manager."""
    check_commands = {
        'apt': ['dpkg-query', '-W', '-f=${Status}', package],
        'dnf': ['dnf', 'list', 'installed', package],
        'pacman': ['pacman', '-Q', package],
        'zypper': ['zypper', 'search', '--installed-only', package]
    }

    if manager not in check_commands:
        raise ValueError(f"Package manager '{manager}' is not supported for checking packages.")

    try:
        result = subprocess.run(check_commands[manager], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if manager == 'apt':
            return "install ok installed" in result.stdout
        elif manager == 'pacman':
            return result.returncode == 0
        else:
            return result.returncode == 0
    except subprocess.CalledProcessError:
        return False


def install_using_package_manager(package, manager, install_cmd):
    """Install a package using the appropriate package manager."""
    if check_package_installed(package, manager):
        print(f"{package} is already installed. No need to reinstall.")
        return

    try:
        print(f'Installing {package} using {manager}')
        subprocess.run(install_cmd + [package], check=True)
        print(f'Package {package} installed successfully.')
    except subprocess.CalledProcessError as e:
        print(f"FAILED! Error installing {package}:\n{e}")


def install_necessary_packages(packages):
    manager, install_cmd = detect_package_manager()

    if manager is None:
        print("No supported package manager found!")
        return

    for package in packages:
        install_using_package_manager(package, manager, install_cmd)

    print('FINISHED! Installing all packages.')