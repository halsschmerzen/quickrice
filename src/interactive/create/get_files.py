import os

class ThemeOptions:
    def __init__(self, theme_dirs):
        self.theme_dirs = theme_dirs
    
    def get_available_themes(self):
        """Fetches available themes from specified directories."""
        themes = set()
        for directory in self.theme_dirs:
            if os.path.exists(directory):
                themes.update(next(os.walk(directory))[1])  # Get directory names
        return list(themes)

    def choose_from_list(self, theme_list, theme_type):
        """Displays a list of themes and allows the user to choose one by number."""
        if not theme_list:
            print(f"No {theme_type} themes available.")
            return None
        print(f"\nAvailable {theme_type} themes:")
        for idx, theme in enumerate(theme_list, start=1):
            print(f"{idx}: {theme}")
        
        while True:
            try:
                choice = int(input(f"Enter the number of the {theme_type} theme you want to select: "))
                if 1 <= choice <= len(theme_list):
                    return theme_list[choice - 1]
                else:
                    print(f"Please choose a number between 1 and {len(theme_list)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

class GnomeThemeOptions(ThemeOptions):
    def __init__(self):
        gtk_theme_dirs = ['/usr/share/themes', os.path.expanduser('~/.themes')]
        icon_theme_dirs = ['/usr/share/icons', os.path.expanduser('~/.icons')]
        super().__init__(gtk_theme_dirs + icon_theme_dirs)
    
    def get_available_gtk_themes(self):
        """Fetches available GTK themes from system and user directories."""
        return self.get_available_themes()

    def get_available_icon_themes(self):
        """Fetches available icon themes from system and user directories."""
        return self.get_available_themes()

    def get_available_shell_themes(self):
        """Fetches available GNOME Shell themes (themes with 'gnome-shell' directory)."""
        shell_themes = set()
        for directory in self.theme_dirs:
            if os.path.exists(directory):
                for theme in next(os.walk(directory))[1]:
                    theme_path = os.path.join(directory, theme, 'gnome-shell')
                    if os.path.exists(theme_path):
                        shell_themes.add(theme)
        return list(shell_themes)

    def get_available_cursor_themes(self):
        """Fetches available cursor themes from system and user directories."""
        cursor_themes = set()
        for directory in self.theme_dirs:
            if os.path.exists(directory):
                for theme in next(os.walk(directory))[1]:
                    theme_path = os.path.join(directory, theme, 'cursors')
                    if os.path.exists(theme_path):
                        cursor_themes.add(theme)
        return list(cursor_themes)