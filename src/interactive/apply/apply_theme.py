from desktop.detect_desktop import return_desktop
from interactive.create.create_desktop import read_theme
from interactive.display_list import choose_from_list
from desktop.desktops import GnomeTheme

import os, json

config_dir = os.path.expanduser('~/.config/quickrice/rices')

def list_available_themes():

    themes_for_this_desktop = []

    current_desktop = 'gnome'

    #Open every file and check for the identifier of the desktop
    for filename in os.listdir(config_dir):
        if filename.endswith('.json'):
            path = os.path.join(config_dir, filename)

            try:

                with open(path, 'r') as json_file:
                    data = json.load(json_file)
                    
                    if 'desktop' in data and data['desktop']==current_desktop:
                        theme_name = os.path.splitext(filename)[0]
                        themes_for_this_desktop.append(theme_name)

            except json.JSONDecodeError:
                print('err')

    return themes_for_this_desktop


def choose_theme():
    available_themes = list_available_themes()

    # Prompt the user to select a theme
    selected_theme_name = choose_from_list(available_themes)

    # Construct the path to the selected theme's JSON file
    selected_theme_path = os.path.join(config_dir, selected_theme_name + '.json')

    # Read the selected theme's values
    try:
        with open(selected_theme_path, 'r') as json_file:
            theme_data = json.load(json_file)

            # Extract relevant values from the JSON data
            selected_gtk_theme = theme_data.get('gtk_theme')  
            selected_icon_theme = theme_data.get('icon_theme')
            selected_shell_theme = theme_data.get('shell_theme')
            selected_cursor_theme = theme_data.get('cursor_theme')

            gnome_theme = GnomeTheme(selected_gtk_theme,selected_icon_theme,selected_cursor_theme,None,None)

            # Apply the selected themes using GnomeTheme methods
            gnome_theme.set_gtk_theme(selected_gtk_theme)
            gnome_theme.set_icon_theme(selected_icon_theme)
            gnome_theme.set_shell_theme(selected_shell_theme)
            gnome_theme.set_cursor_theme(selected_cursor_theme)


    except FileNotFoundError:
        print(f'The selected theme file does not exist: {selected_theme_path}')
    except json.JSONDecodeError:
        print(f'Error decoding JSON in file: {selected_theme_path}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')
    
    


