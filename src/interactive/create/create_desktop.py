from desktop.detect_desktop import return_desktop
from desktop.desktops import GnomeTheme
from interactive.create.get_files import GnomeThemeOptions
import os, json

config_dir = os.path.expanduser('~/.config/quickrice/rices')

def create_new_rice():
    current_desktop = return_desktop()

    if current_desktop == 'kde':
        create_gnome_theme()
    else:
        print('Currently not supported!')


def create_gnome_theme():
    theme_options = GnomeThemeOptions()

    gtk_themes = theme_options.get_available_gtk_themes()
    icon_themes = theme_options.get_available_icon_themes()
    shell_themes = theme_options.get_available_shell_themes()
    cursor_themes = theme_options.get_available_cursor_themes()

    selected_gtk_theme = theme_options.choose_from_list(gtk_themes, "GTK")
    selected_icon_theme = theme_options.choose_from_list(icon_themes, "Icon")
    selected_shell_theme = theme_options.choose_from_list(shell_themes, "Shell")
    selected_cursor_theme = theme_options.choose_from_list(cursor_themes, "Cursor")

    selections = {
        "desktop" : "gnome",
        "gtk_theme": selected_gtk_theme,
        "icon_theme": selected_icon_theme,
        "shell_theme": selected_shell_theme,
        "cursor_theme": selected_cursor_theme,
    }

    while True:
        theme_name = str(input('Enter the rice name: '))
        
        if os.path.exists(f'{config_dir}/{theme_name}.json'):
            print('Theme with that name already exists!')
        else:
            write_to_json(selections, theme_name)
            break
         

def write_to_json(theme_properties: dict, name):
    
    json_file_path = os.path.join(config_dir, f'{name}.json')

    os.makedirs(config_dir, exist_ok=True)

    with open(json_file_path, 'w') as json_file:
        json.dump(theme_properties, json_file, indent=4)

    print(f'Written data to: {json_file_path}')

def read_theme(name):
    json_file_path = os.path.join(config_dir, f'{name}.json')

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    return data
