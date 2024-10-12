import os

class GnomeThemeOptions:
    def __init__(self):
        self.gtk_theme_dirs = ['/usr/share/themes', os.path.expanduser('~/.themes')]
        self.icon_theme_dirs = ['/usr/share/icons', os.path.expanduser('~/.icons')]
    
    def get_available_gtk_themes(self):
        """Fetches available GTK themes from system and user directories."""
        gtk_themes = set()
        for directory in self.gtk_theme_dirs:
            if os.path.exists(directory):
                gtk_themes.update(next(os.walk(directory))[1])  # Get directory names
        return list(gtk_themes)
    
    def get_available_icon_themes(self):
        """Fetches available icon themes from system and user directories."""
        icon_themes = set()
        for directory in self.icon_theme_dirs:
            if os.path.exists(directory):
                icon_themes.update(next(os.walk(directory))[1])
        return list(icon_themes)

    def get_available_shell_themes(self):
        """Fetches available GNOME Shell themes (themes with 'gnome-shell' directory)."""
        shell_themes = set()
        for directory in self.gtk_theme_dirs:
            if os.path.exists(directory):
                for theme in next(os.walk(directory))[1]:
                    theme_path = os.path.join(directory, theme, 'gnome-shell')
                    if os.path.exists(theme_path):
                        shell_themes.add(theme)
        return list(shell_themes)

    def get_available_cursor_themes(self):
        """Fetches available cursor themes from system and user directories."""
        cursor_themes = set()
        for directory in self.icon_theme_dirs:
            if os.path.exists(directory):
                for theme in next(os.walk(directory))[1]:
                    theme_path = os.path.join(directory, theme, 'cursors')
                    if os.path.exists(theme_path):
                        cursor_themes.add(theme)
        return list(cursor_themes)

