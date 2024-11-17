import os
from interactive.create.get_files import ThemeOptions

class XfceThemeOptions(ThemeOptions):
    def __init__(self):
        gtk_theme_dirs = ['/usr/share/themes', os.path.expanduser('~/.themes')]
        icon_theme_dirs = ['/usr/share/icons', os.path.expanduser('~/.icons')]
        super().__init__(gtk_theme_dirs + icon_theme_dirs)
        self.gtk_theme_dirs = gtk_theme_dirs
        self.icon_theme_dirs = icon_theme_dirs

    @staticmethod
    def is_valid_gtk_theme(theme_path):
        """Checks if the theme contains valid GTK theme files."""
        return any(
            os.path.exists(os.path.join(theme_path, f"gtk-{version}/gtk.css"))
            for version in ['3.0', '4.0']
        )

    @staticmethod
    def is_valid_icon_theme(theme_path):
        """Checks if the theme contains a valid icon theme file."""
        return os.path.exists(os.path.join(theme_path, "index.theme"))

    @staticmethod
    def is_valid_xfwm4_theme(theme_path):
        """Checks if the theme contains valid XFWM4 theme files."""
        xfwm4_theme_path = os.path.join(theme_path, 'xfwm4')
        return os.path.exists(xfwm4_theme_path) and os.path.exists(os.path.join(xfwm4_theme_path, 'themerc'))

    @staticmethod
    def is_valid_cursor_theme(theme_path):
        """Checks if the theme contains a valid cursor theme."""
        cursor_path = os.path.join(theme_path, 'cursors')
        return os.path.exists(cursor_path) and any(os.path.isfile(os.path.join(cursor_path, file)) for file in ['arrow', 'default'])

    # Methods for fetching themes
    def get_available_gtk_themes(self):
        """Fetches available GTK themes from system and user directories, validating them."""
        return self.get_available_themes(self.gtk_theme_dirs, validation_func=self.is_valid_gtk_theme)

    def get_available_icon_themes(self):
        """Fetches available icon themes from system and user directories, validating them."""
        return self.get_available_themes(self.icon_theme_dirs, validation_func=self.is_valid_icon_theme)

    def get_available_xfwm4_themes(self):
        """Fetches available XFWM4 themes, validating them."""
        return self.get_available_themes(self.gtk_theme_dirs, validation_func=self.is_valid_xfwm4_theme)

    def get_available_cursor_themes(self):
        """Fetches available cursor themes, validating them."""
        return self.get_available_themes(self.icon_theme_dirs, validation_func=self.is_valid_cursor_theme)