import os

class DesktopTheme:
    def __init__(self, gtk_theme, icon_theme, cursor_theme, font, color_scheme):
        self.gtk_theme = gtk_theme
        self.icon_theme = icon_theme
        self.cursor_theme = cursor_theme
        self.font = font
        self.color_scheme = color_scheme

    def apply_theme(self):
        """Applies the current theme settings."""
        self.set_gtk_theme(self.gtk_theme)
        self.set_icon_theme(self.icon_theme)
        self.set_cursor_theme(self.cursor_theme)
        self.set_font(self.font)
        self.set_color_scheme(self.color_scheme)
        print("Theme applied successfully")

    def set_gtk_theme(self, theme_name):
        """Sets the GTK theme."""
        print(f"Setting GTK theme to {theme_name}")
        raise NotImplementedError("This method should be implemented by a subclass")

    def set_icon_theme(self, theme_name):
        """Sets the icon theme."""
        print(f"Setting Icon theme to {theme_name}")
        raise NotImplementedError("This method should be implemented by a subclass")

    def set_cursor_theme(self, theme_name):
        """Sets the cursor theme."""
        print(f"Setting Cursor theme to {theme_name}")
        raise NotImplementedError("This method should be implemented by a subclass")

    def set_font(self, font_name):
        """Sets the default UI font."""
        print(f"Setting UI Font to {font_name}")
        raise NotImplementedError("This method should be implemented by a subclass")

    def set_color_scheme(self, scheme):
        """Sets the color scheme (light or dark)."""
        print(f"Setting color scheme to {scheme}")
        raise NotImplementedError("This method should be implemented by a subclass")

    def reset_to_default(self):
        """Resets theme settings to desktop defaults."""
        print("Resetting to default theme")
        raise NotImplementedError("This method should be implemented by a subclass")

# Cinnamon subclass
class CinnamonTheme(DesktopTheme):
    def set_gtk_theme(self, theme_name):
        os.system(f"gsettings set org.cinnamon.desktop.interface gtk-theme {theme_name}")

    def set_icon_theme(self, theme_name):
        os.system(f"gsettings set org.cinnamon.desktop.interface icon-theme {theme_name}")
        
    def set_shell_theme(self, theme_name):
        os.system(f"gsettings set org.cinnamon.theme name {theme_name}")

    def set_cursor_theme(self, theme_name):
        os.system(f"gsettings set org.cinnamon.desktop.interface cursor-theme {theme_name}")

    def set_font(self, font_name):
        os.system(f"gsettings set org.cinnamon.desktop.interface font-name '{font_name} 11'")

    def reset_to_default(self):
        self.gtk_theme = "Mint-Y"
        self.icon_theme = "Mint-Y"
        self.cursor_theme = "DMZ-White"
        self.font = "Cantarell"
        self.apply_theme()

# GNOME subclass
class GnomeTheme(DesktopTheme):
    def set_gtk_theme(self, theme_name):
        os.system(f"gsettings set org.gnome.desktop.interface gtk-theme {theme_name}")

    def set_icon_theme(self, theme_name):
        os.system(f"gsettings set org.gnome.desktop.interface icon-theme {theme_name}")

    def set_cursor_theme(self, theme_name):
        os.system(f"gsettings set org.gnome.desktop.interface cursor-theme {theme_name}")

    def set_font(self, font_name):
        os.system(f"gsettings set org.gnome.desktop.interface font-name '{font_name} 11'")

    def set_color_scheme(self, scheme):
        if scheme == "dark":
            os.system("gsettings set org.gnome.desktop.interface color-scheme prefer-dark")
        else:
            os.system("gsettings set org.gnome.desktop.interface color-scheme prefer-light")

    def set_shell_theme(self, theme_name):
        os.system(f"gsettings set org.gnome.shell.extensions.user-theme name {theme_name}")

    def set_wallpaper(self, wallpaper_path, scheme):
        if scheme == "dark":
            os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark 'file://{wallpaper_path}'")
        else:
            os.system(f"gsettings set org.gnome.desktop.background picture-uri 'file://{wallpaper_path}'")

    def reset_to_default(self):
        self.gtk_theme = "Adwaita"
        self.icon_theme = "Adwaita"
        self.cursor_theme = "Adwaita"
        self.font = "Cantarell"
        self.color_scheme = "light"
        self.apply_theme()
