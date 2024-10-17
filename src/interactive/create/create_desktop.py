from desktop.detect_desktop import return_desktop
from desktop.desktops import GnomeTheme
from interactive.create.desktop_options.gnome_theme import GnomeThemeOptions
import os, json, subprocess

config_dir = os.path.expanduser('~/.config/quickrice/rices')

def create_new_rice():
    current_desktop = return_desktop()

    if current_desktop == 'gnome':
        create_gnome_theme()
    else:
        print('Currently not supported!')

def is_user_themes_enabled():
    try:
        # Read the current state of the User Themes extension
        result = subprocess.run(
            ["dconf", "read", "/org/gnome/shell/extensions/user-theme/enable"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip() == "true"
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while checking the status: {e}")
        return False

def enable_user_themes():
    if is_user_themes_enabled():
        print("User Themes extension is already enabled.")
        return

    user_input = input("User Themes extension is not enabled. Do you want to enable it? (y/n): ").strip().lower()
    
    if user_input in ['yes', 'y']:
        os.system("dconf write /org/gnome/shell/extensions/user-theme/enable true")
        print("User Themes extension has been enabled.")
    else:
        return

def create_gnome_theme():
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
