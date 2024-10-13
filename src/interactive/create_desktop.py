from desktop.detect_desktop import return_desktop
from desktop.desktops import GnomeTheme
from interactive.get_files import GnomeThemeOptions
import os, json

def create_new_rice():
    current_desktop = return_desktop

    if current_desktop == 'gnome':
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
        "gtk_theme": selected_gtk_theme,
        "icon_theme": selected_icon_theme,
        "shell_theme": selected_shell_theme,
        "cursor_theme": selected_cursor_theme,
    }

    rice_name = str(input('Enter the rice name. '))

    with open(f"{rice_name}.json", "w") as json_file:
        json.dump(selections, json_file, indent=4)

    print(f"Selected themes saved to '{rice_name}.json'.")