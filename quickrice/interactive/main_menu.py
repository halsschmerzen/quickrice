from quickrice.desktop.detect_desktop import return_desktop
from quickrice.interactive.create.create_desktop import create_new_rice, read_theme
from quickrice.interactive.apply.apply_theme import list_available_themes, choose_gnome_theme, choose_cinnamon_theme, create_config_directory
from quickrice.desktop.extensions.check_system import detect_package_manager, collect_necessary_packages
from quickrice.desktop.extensions.download_extensions import check_package_installed, install_necessary_packages
import re

package_manager, install_command = detect_package_manager()
necessary_packages = collect_necessary_packages(package_manager)
packages_needed = False 

def banner():
    return r'''

                    _     __  
         ___ ___ __(_)___/ /__
        / _ `/ // / / __/  '_/
        \_, /\_,_/_/\__/_/\_\ 
         /_/  ____(_)______   
             / __/ / __/ -_)  
            /_/ /_/\__/\__/   

        quickrice! A simple and quick way to
        change your rice from the CLI.                               
    '''

def display_main():
    global package_manager, necessary_packages
    print(banner())
    create_config_directory()

    # Check for installed packages and collect the ones that are not installed
    packages_to_install = []
    
    for pkg in necessary_packages:  # necessary_packages should be defined beforehand
        if not check_package_installed(pkg, package_manager):
            packages_to_install.append(pkg)

    if packages_to_install:
        print(f"Installing necessary packages: {packages_to_install}")
        install_necessary_packages(packages_to_install)
    else:
        print("All necessary packages are already installed.")

    # Mapping of desktop patterns to theme application functions
    desktop_theme_functions = {
        r'gnome.*|ubuntu': choose_gnome_theme,
        r'cinnamon': choose_cinnamon_theme,
        # Add other desktop patterns and their corresponding functions here
    }

    while True:
        desktop = return_desktop().lower()
        print('====================================================')
        print(f'You are currently on {desktop}. ')
        print('====================================================')
        print('Choose your option:')
        print('1 - Generate new rice')
        print('2 - Apply existing rice')
        print('====================================================')
        option = int(input('Enter your choice: '))

        if option == 1:
            create_new_rice()
        elif option == 2:
            for pattern, func in desktop_theme_functions.items():
                if re.match(pattern, desktop):
                    func()
                    break
            else:
                print('Desktop not supported yet!')
        else:
            print('Invalid option. Please try again.')