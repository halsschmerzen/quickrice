import os
import requests
import zipfile
import tarfile
from pathlib import Path
import shutil

class Theme:
    def __init__(self, name, gtk_link, icon_link, cursor_link, shell_link):
        self.name = name  # Name of the complete theme
        self.gtk_link = gtk_link  # Download link for GTK theme
        self.icon_link = icon_link  # Download link for Icons
        self.cursor_link = cursor_link  # Download link for Cursors
        self.shell_link = shell_link  # Download link for Shell theme

    def get_download_links(self):
        """Return a dictionary of all download links."""
        return {
            'GTK': self.gtk_link,
            'Icons': self.icon_link,
            'Cursors': self.cursor_link,
            'Shell': self.shell_link
        }

    def validate_theme(self, extract_path, theme_type):
        """Check if the directory contains valid theme files."""
        if theme_type == 'GTK':
            return any((extract_path / d).exists() for d in ['gtk-3.0', 'gtk-2.0'])

        elif theme_type == 'Icons':
            return (extract_path / 'index.theme').exists()

        elif theme_type == 'Cursors':
            return (extract_path / 'cursors').exists()

        elif theme_type == 'Shell':
            return (extract_path / 'gnome-shell').exists()

        return False

    def download_and_install(self):
        """Download and install the theme components."""
        download_links = self.get_download_links()

        themes_dir = Path.home() / ".themes"
        icons_dir = Path.home() / ".icons"
        shell_dir = Path.home() / ".local/share/gnome-shell/extensions"

        themes_dir.mkdir(parents=True, exist_ok=True)
        icons_dir.mkdir(parents=True, exist_ok=True)
        shell_dir.mkdir(parents=True, exist_ok=True)

        for theme_type, url in download_links.items():
            print(f"Downloading {theme_type} from {url}...")
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses

            # Determine the file extension to handle extraction
            filename = url.split("/")[-1]
            filepath = Path.home() / filename
            
            # Save the file
            with open(filepath, 'wb') as file:
                file.write(response.content)

            # Extract files based on the file type
            temp_dir = Path.home() / "temp_extracted"
            temp_dir.mkdir(parents=True, exist_ok=True)

            try:
                if filename.endswith('.zip'):
                    with zipfile.ZipFile(filepath, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)
                elif filename.endswith('.tar.gz'):
                    with tarfile.open(filepath, 'r:gz') as tar_ref:
                        tar_ref.extractall(temp_dir)
                elif filename.endswith('.tar'):
                    with tarfile.open(filepath, 'r:') as tar_ref:
                        tar_ref.extractall(temp_dir)
                else:
                    print(f"Warning: Unsupported file type for {filename}.")
                    continue
            except Exception as e:
                print(f"Error extracting {filename}: {e}")
                continue

            # Move valid themes to the appropriate directories
            for extracted_theme in temp_dir.iterdir():
                if extracted_theme.is_dir():
                    if self.validate_theme(extracted_theme, 'GTK'):
                        shutil.move(str(extracted_theme), str(themes_dir / extracted_theme.name))
                        print(f"GTK Theme {extracted_theme.name} installed successfully at {themes_dir / extracted_theme.name}.")
                    elif self.validate_theme(extracted_theme, 'Icons'):
                        shutil.move(str(extracted_theme), str(icons_dir / extracted_theme.name))
                        print(f"Icon Theme {extracted_theme.name} installed successfully at {icons_dir / extracted_theme.name}.")
                    elif self.validate_theme(extracted_theme, 'Cursors'):
                        shutil.move(str(extracted_theme), str(icons_dir / extracted_theme.name))
                        print(f"Cursor Theme {extracted_theme.name} installed successfully at {icons_dir / extracted_theme.name}.")
                    elif self.validate_theme(extracted_theme, 'Shell'):
                        shutil.move(str(extracted_theme), str(shell_dir / extracted_theme.name))
                        print(f"Shell Theme {extracted_theme.name} installed successfully at {shell_dir / extracted_theme.name}.")
                    else:
                        print(f"Warning: {extracted_theme.name} is not a valid theme.")

            # Clean up
            shutil.rmtree(temp_dir)  # Remove temporary extraction directory
            os.remove(filepath)       # Remove the downloaded file

    def __str__(self):
        return f"Theme: {self.name}\n" \
               f"  GTK: {self.gtk_link}\n" \
               f"  Icons: {self.icon_link}\n" \
               f"  Cursors: {self.cursor_link}\n" \
               f"  Shell: {self.shell_link}\n"
