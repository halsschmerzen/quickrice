import os
from quickrice.interactive.create.get_files import ThemeOptions

class GnomeThemeOptions(ThemeOptions):
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
    

    def check_if_shell_extension(self, extension_id='user-theme@gnome-shell-extensions.gcampax.github.com'):
        # Directories to check
        user_dir = os.path.expanduser('~/.local/share/gnome-shell/extensions/')
        system_dir = '/usr/share/gnome-shell/extensions/'
        
        # Full paths for user-specific and system-wide extensions
        user_extension_path = os.path.join(user_dir, extension_id)
        system_extension_path = os.path.join(system_dir, extension_id)

        # Check if extension exists in user-specific or system-wide directories
        if os.path.exists(user_extension_path):
            return f"Extension '{extension_id}' is installed in the user directory."
        elif os.path.exists(system_extension_path):
            return f"Extension '{extension_id}' is installed system-wide."
        else:
            message = f'''User Theme Extension has not been found! Install it now from:

            https://extensions.gnome.org/extension/19/user-themes/

            Otherwise, the Shell theme will not be present.

            Perhaps one day I can install it automatically from here...
            '''
            return message



    @staticmethod
    def is_valid_icon_theme(theme_path):
        """Checks if the theme contains a valid icon theme file."""
        return os.path.exists(os.path.join(theme_path, "index.theme"))

    @staticmethod
    def is_valid_shell_theme(theme_path):
        """Checks if the theme contains valid GNOME Shell theme files."""
        shell_theme_path = os.path.join(theme_path, 'gnome-shell')
        return os.path.exists(shell_theme_path) and os.path.exists(os.path.join(shell_theme_path, 'gnome-shell.css'))

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

    def get_available_shell_themes(self):
        """Fetches available GNOME Shell themes, validating them."""
        return self.get_available_themes(self.gtk_theme_dirs, validation_func=self.is_valid_shell_theme)

    def get_available_cursor_themes(self):
        """Fetches available cursor themes, validating them."""
        return self.get_available_themes(self.icon_theme_dirs, validation_func=self.is_valid_cursor_theme)
    


