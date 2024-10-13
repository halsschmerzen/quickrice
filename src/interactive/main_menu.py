from desktop.detect_desktop import return_desktop
from desktop.desktops import GnomeTheme, CinnamonTheme
from interactive.get_files import GnomeThemeOptions
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
    theme_options = GnomeThemeOptions()

    gtk_themes = theme_options.get_available_gtk_themes()
    icon_themes = theme_options.get_available_icon_themes()
    shell_themes = theme_options.get_available_shell_themes()
    cursor_themes = theme_options.get_available_cursor_themes()

    print(gtk_themes)
    print(icon_themes)
    print(shell_themes)
    print(cursor_themes)

    if desktop == 'gnome':
        try:
            theme = GnomeTheme(gtk_theme=random.choice(gtk_themes),icon_theme=random.choice(icon_themes),shell_theme=shell_themes[0], cursor_theme=random.choice(cursor_themes), font='Cantarell', color_scheme='dark')
            theme.apply_theme()
        except ValueError as e:
            print(f'Error {e}')

    if desktop == 'cinnamon':
        try:
            theme = CinnamonTheme(gtk_theme=random.choice(gtk_themes),icon_theme=random.choice(icon_themes),shell_theme=shell_themes[0], cursor_theme=random.choice(cursor_themes), font='Cantarell', color_scheme='dark')
            theme.apply_theme()
        except ValueError as e:
            print(f'Error {e}')

    



