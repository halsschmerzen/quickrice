from desktop.detect_desktop import return_desktop
from interactive.create.create_desktop import create_new_rice, read_theme
from interactive.apply.apply_theme import list_available_themes, choose_gnome_theme, create_config_directory
from desktop.extensions.check_system import check_package_manager

def banner():

    return '''
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
    print(banner())
    create_config_directory()

    while True:
        desktop = return_desktop()
        package_manager = check_package_manager()

        print(f'Current Package Manager {package_manager}')

        print(f'You are currently on {desktop}. ')
        option = int(input('Choose your option:\n1 - gen rice\n2- apply rice'))

        if option==1:
            create_new_rice()
        elif option == 2:
            #This needs to be mapped according to the current desktop.
            #For now only GNOME is supported so this is fine.
            choose_gnome_theme()


