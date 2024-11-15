import os
import json
import subprocess
import re
from desktop.detect_desktop import return_desktop
from interactive.create.desktop_options.gnome_theme import GnomeThemeOptions
from interactive.create.desktop_options.cinnamon_theme import CinnamonThemeOptions

config_dir = os.path.expanduser('~/.config/quickrice/rices')

def create_new_rice():
    current_desktop = return_desktop().lower()
    
    available_desktops = {
        r'gnome.*|ubuntu' : create_gnome_theme,
        r'cinnamon' : create_cinnamon_theme,
    }

    for pattern, method in available_desktops.items():
        if re.match(pattern, current_desktop):
            method(current_desktop)
            break
    else:
        print('Desktop not supported yet!')

def create_gnome_theme(current_desktop):
    theme_options = GnomeThemeOptions()

    if not is_user_themes_enabled():
        enable_user_themes()

    print(theme_options.check_if_shell_extension())

    gtk_themes = theme_options.get_available_gtk_themes()
    icon_themes = theme_options.get_available_icon_themes()
    shell_themes = theme_options.get_available_shell_themes()
    cursor_themes = theme_options.get_available_cursor_themes()

    selected_gtk_theme = theme_options.choose_from_list(gtk_themes, "GTK")
    selected_icon_theme = theme_options.choose_from_list(icon_themes, "Icon")
    selected_shell_theme = theme_options.choose_from_list(shell_themes, "Shell")
    selected_cursor_theme = theme_options.choose_from_list(cursor_themes, "Cursor")
    selected_font = None
    selected_color_scheme = 'dark'
    selected_background = None

    font_input = str(input('Do you want to set a Font? [y/n]'))

    if font_input == 'y':
        font_value = str(input('Please enter the name of the font you want to apply: \n'))
        selected_font = font_value

    color_input = str(input('Do you want the preferred color scheme to be light? [Default Value: Dark] [y/n]'))
    if color_input == 'y':
        selected_color_scheme = 'light'
            
    bg_input = str(input('Do you want to set a matching wallpaper? [y/n]'))
    if bg_input == 'y':
        background_path = str(input('Enter the path to the desired wallpaper: \n'))
        selected_background = background_path

    selections = {
        "desktop" : "gnome",
        "gtk_theme": selected_gtk_theme,
        "icon_theme": selected_icon_theme,
        "shell_theme": selected_shell_theme,
        "cursor_theme": selected_cursor_theme,
        "font": selected_font,
        "color_scheme": selected_color_scheme,
        "background": selected_background
    }

    desktop_dir = os.path.join(config_dir, "gnome")
    os.makedirs(desktop_dir, exist_ok=True)

    while True:
        theme_name = str(input('Enter the rice name: '))
        
        if os.path.exists(f'{desktop_dir}/{theme_name}.json'):
            print('Theme with that name already exists!')
        else:
            write_to_json(selections, theme_name, desktop_dir)
            break

def create_cinnamon_theme(current_desktop):
    theme_options = CinnamonThemeOptions()

    gtk_themes = theme_options.get_available_gtk_themes()
    icon_themes = theme_options.get_available_icon_themes()
    shell_themes = theme_options.get_available_shell_themes()
    cursor_themes = theme_options.get_available_cursor_themes()

    selected_gtk_theme = theme_options.choose_from_list(gtk_themes, "GTK")
    selected_icon_theme = theme_options.choose_from_list(icon_themes, "Icon")
    selected_shell_theme = theme_options.choose_from_list(shell_themes, "Shell")
    selected_cursor_theme = theme_options.choose_from_list(cursor_themes, "Cursor")
    selected_font = None
    selected_color_scheme = 'dark'
    selected_background = None

    font_input = str(input('Do you want to set a Font? [y/n]'))

    if font_input == 'y':
        font_value = str(input('Please enter the name of the font you want to apply: \n'))
        selected_font = font_value

    color_input = str(input('Do you want the preferred color scheme to be light? [Default Value: Dark] [y/n]'))
    if color_input == 'y':
        selected_color_scheme = 'light'
            
    bg_input = str(input('Do you want to set a matching wallpaper? [y/n]'))
    if bg_input == 'y':
        background_path = str(input('Enter the path to the desired wallpaper: \n'))
        selected_background = background_path

    selections = {
        "desktop" : "cinnamon",
        "gtk_theme": selected_gtk_theme,
        "icon_theme": selected_icon_theme,
        "shell_theme": selected_shell_theme,
        "cursor_theme": selected_cursor_theme,
        "font": selected_font,
        "color_scheme": selected_color_scheme,
        "background": selected_background
    }

    desktop_dir = os.path.join(config_dir, "cinnamon")
    os.makedirs(desktop_dir, exist_ok=True)

    while True:
        theme_name = str(input('Enter the rice name: '))
        
        if os.path.exists(f'{desktop_dir}/{theme_name}.json'):
            print('Theme with that name already exists!')
        else:
            write_to_json(selections, theme_name, desktop_dir)
            break

def write_to_json(theme_properties: dict, name, desktop_dir):
    json_file_path = os.path.join(desktop_dir, f'{name}.json')

    os.makedirs(desktop_dir, exist_ok=True)

    with open(json_file_path, 'w') as json_file:
        json.dump(theme_properties, json_file, indent=4)

    print(f'Written data to: {json_file_path}')

def read_theme(name):
    json_file_path = os.path.join(config_dir, f'{name}.json')

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    return data
