import os

class GnomeTheme:
    def __init__(self, gtk_theme, icon_theme, shell_theme, cursor_theme, font, color_scheme):
        if not gtk_theme:
            raise ValueError("GTK theme must not be empty")
        if not icon_theme:
            raise ValueError("Icon theme must not be empty")
        if not shell_theme:
            raise ValueError("Shell theme must not be empty")
        if not cursor_theme:
            raise ValueError("Cursor theme must not be empty")
        if not font:
            raise ValueError("Font must not be empty")
        if color_scheme not in ["light", "dark"]:
            raise ValueError("Color scheme must be either 'light' or 'dark'")
        

        self.gtk_theme = gtk_theme
        self.icon_theme = icon_theme
        self.shell_theme = shell_theme
        self.cursor_theme = cursor_theme
        self.font = font
        self.color_scheme = color_scheme

    def apply_theme(self):
        """Applies the current theme settings."""
        self.set_gtk_theme(self.gtk_theme)
        self.set_icon_theme(self.icon_theme)
        self.set_shell_theme(self.shell_theme)
        self.set_cursor_theme(self.cursor_theme)
        self.set_font(self.font)
        self.set_color_scheme(self.color_scheme)
        print("Theme applied successfully")

    def set_gtk_theme(self, theme_name):
        """Sets the GTK theme."""
        print(f"Setting GTK theme to {theme_name}")
        os.system(f"gsettings set org.gnome.desktop.interface gtk-theme {theme_name}")

    def set_icon_theme(self, theme_name):
        """Sets the icon theme."""
        print(f"Setting Icon theme to {theme_name}")
        os.system(f"gsettings set org.gnome.desktop.interface icon-theme {theme_name}")

    def set_shell_theme(self, theme_name):
        """Sets the GNOME Shell theme."""
        print(f"Setting Shell theme to {theme_name}")
        os.system(f"gsettings set org.gnome.shell.extensions.user-theme name {theme_name}")

    def set_cursor_theme(self, theme_name):
        """Sets the cursor theme."""
        print(f"Setting Cursor theme to {theme_name}")
        os.system(f"gsettings set org.gnome.desktop.interface cursor-theme {theme_name}")

    def set_font(self, font_name):
        """Sets the default UI font."""
        print(f"Setting UI Font to {font_name}")
        os.system(f"gsettings set org.gnome.desktop.interface font-name '{font_name} 11'")

    def set_color_scheme(self, scheme):
        """Sets the color scheme (light or dark)."""
        print(f"Setting color scheme to {scheme}")
        if scheme == "dark":
            os.system("gsettings set org.gnome.desktop.interface color-scheme prefer-dark")
        else:
            os.system("gsettings set org.gnome.desktop.interface color-scheme prefer-light")

    def reset_to_default(self):
        """Resets theme settings to GNOME defaults."""
        print("Resetting to default GNOME theme")
        self.gtk_theme = "Adwaita"
        self.icon_theme = "Adwaita"
        self.shell_theme = "Adwaita"
        self.cursor_theme = "Adwaita"
        self.font = "Cantarell"
        self.color_scheme = "light"
        self.apply_theme()


