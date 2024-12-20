import os
import json
import re
from desktop.detect_desktop import return_desktop
from interactive.create.create_desktop import read_theme
from interactive.display_list import choose_from_list
from desktop.desktops import GnomeTheme, CinnamonTheme, XfceTheme

config_dir = os.path.expanduser('~/.config/quickrice/rices')

def create_config_directory():
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

def apply_theme_by_name(theme_name):
    current_desktop = return_desktop().lower()

    desktop_patterns = {
        'gnome': [r'gnome.*', r'ubuntu'],
        'cinnamon': [r'cinnamon'],
        'xfce': [r'xfce'],
        # Add other desktop patterns and their corresponding functions here
    }

    desktop_dir = None
    apply_theme_func = None

    for desktop, patterns in desktop_patterns.items():
        for pattern in patterns:
            if re.match(pattern, current_desktop):
                desktop_dir = os.path.join(config_dir, desktop)
                apply_theme_func = globals().get(f'apply_{desktop}_theme')
                break
        if desktop_dir:
            break
    else:
        print('Desktop not supported yet!')
        return

    if not desktop_dir or not os.path.exists(desktop_dir):
        print('No themes directory found for your desktop environment.')
        return

    theme_file = os.path.join(desktop_dir, theme_name + '.json')
    if not os.path.exists(theme_file):
        print(f'Theme "{theme_name}" not found in {desktop_dir}.')
        return

    try:
        with open(theme_file, 'r') as json_file:
            theme_data = json.load(json_file)
            if apply_theme_func:
                apply_theme_func(theme_data)
            else:
                print('No function available to apply theme for your desktop environment.')
    except json.JSONDecodeError:
        print(f'Error decoding JSON in file: {theme_file}')

def list_available_themes():
    themes_for_this_desktop = []
    current_desktop = return_desktop().lower()
    
    desktop_patterns = {
        'gnome': [r'gnome.*', r'ubuntu', r'mint'],
        'cinnamon': [r'cinnamon'],
        'xfce': [r'xfce'],
    }

    desktop_dir = None
    for desktop, patterns in desktop_patterns.items():
        for pattern in patterns:
            if re.match(pattern, current_desktop):
                desktop_dir = os.path.join(config_dir, desktop)
                break
        else:
            continue
        break
    else:
        print('Desktop not supported yet!')
        return themes_for_this_desktop

    # Check if the directory is empty
    if not os.path.exists(desktop_dir) or not os.listdir(desktop_dir):
        print('You haven\'t created any themes yet!')
        return themes_for_this_desktop

    for filename in os.listdir(desktop_dir):
        if filename.endswith('.json'):
            path = os.path.join(desktop_dir, filename)
            try:
                with open(path, 'r') as json_file:
                    data = json.load(json_file)
                    if 'desktop' in data:
                        for pattern in patterns:
                            if re.match(pattern, data['desktop']):
                                theme_name = os.path.splitext(filename)[0]
                                themes_for_this_desktop.append(theme_name)
                                break
            except json.JSONDecodeError:
                print(f'Error decoding JSON in file: {filename}')
    return themes_for_this_desktop

def apply_theme(theme_data, theme_class):
    selected_gtk_theme = theme_data.get('gtk_theme')
    selected_icon_theme = theme_data.get('icon_theme')
    selected_shell_theme = theme_data.get('shell_theme')
    selected_xfwm4_theme = theme_data.get('xfwm4_theme')
    selected_cursor_theme = theme_data.get('cursor_theme')
    selected_font = theme_data.get('font')
    selected_color = theme_data.get('color_scheme')
    selected_background = theme_data.get('background')

    theme = theme_class(
        selected_gtk_theme,
        selected_icon_theme,
        selected_cursor_theme,
        selected_font,
        selected_color
    )

    # Apply the selected themes using the theme class methods
    theme.set_gtk_theme(selected_gtk_theme)
    theme.set_icon_theme(selected_icon_theme)
    if hasattr(theme, 'set_shell_theme'):
        theme.set_shell_theme(selected_shell_theme)
    if hasattr(theme, 'set_xfwm4_theme'):
        theme.set_xfwm4_theme(selected_xfwm4_theme)
    theme.set_cursor_theme(selected_cursor_theme)
    theme.set_color_scheme(selected_color)

    if selected_font:
        theme.set_font(selected_font)
    else:
        theme.set_font('Cantarell')

    if selected_background:
        theme.set_wallpaper(selected_background, selected_color)

def choose_theme():
    available_themes = list_available_themes()
    if not available_themes:
        print('You have not created any themes yet!')
        return

    selected_theme_name = choose_from_list(available_themes)

    if selected_theme_name is None:
        print('No theme selected.')
        return

    apply_theme_by_name(selected_theme_name)

def apply_gnome_theme(theme_data):
    apply_theme(theme_data, GnomeTheme)

def apply_cinnamon_theme(theme_data):
    apply_theme(theme_data, CinnamonTheme)

def apply_xfce_theme(theme_data):
    apply_theme(theme_data, XfceTheme)