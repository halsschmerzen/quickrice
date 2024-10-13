from desktop.detect_desktop import return_desktop
from desktop.desktops import GnomeTheme, CinnamonTheme
from interactive.get_files import GnomeThemeOptions
from interactive.create_desktop import create_new_rice
import random

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

    desktop = return_desktop()

    print(f'You are currently on {desktop}. ')

    # Example usage:
    create_new_rice()

    



