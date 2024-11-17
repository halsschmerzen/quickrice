# import os
# import requests
# import zipfile
# import tarfile
# from pathlib import Path
# import shutil

# class Theme:
#     def __init__(self, name, gtk_link, icon_link, cursor_link, shell_link):
#         self.name = name  # Name of the complete theme
#         self.gtk_link = gtk_link  # Download link for GTK theme
#         self.icon_link = icon_link  # Download link for Icons
#         self.cursor_link = cursor_link  # Download link for Cursors
#         self.shell_link = shell_link  # Download link for Shell theme

#     def get_download_links(self):
#         """Return a dictionary of all download links."""
#         return {
#             'GTK': self.gtk_link,
#             'Icons': self.icon_link,
#             'Cursors': self.cursor_link,
#             'Shell': self.shell_link
#         }

#     def validate_theme(self, extract_path, theme_type):
#         """Check if the directory contains valid theme files."""
#         if theme_type == 'GTK':
#             return any((extract_path / d).exists() for d in ['gtk-3.0', 'gtk-2.0'])

#         elif theme_type == 'Icons':
#             return (extract_path / 'index.theme').exists()

#         elif theme_type == 'Cursors':
#             return (extract_path / 'cursors').exists()

#         elif theme_type == 'Shell':
#             return (extract_path / 'gnome-shell').exists()

#         return False

#     def handle_existing_theme(self, theme_dir):
#         """Prompt user about handling existing theme directories."""
#         if theme_dir.exists():
#             response = input(f"{theme_dir.name} already exists. Do you want to overwrite (O), rename (R), or skip (S)? ").strip().lower()
#             if response == 'o':
#                 # Overwrite the existing theme
#                 shutil.rmtree(theme_dir)  # Remove existing theme directory
#             elif response == 'r':
#                 # Rename new theme directory to avoid conflict
#                 new_name = input("Enter a new name for the theme: ").strip()
#                 theme_dir = theme_dir.parent / new_name  # Update path with new name
#                 if theme_dir.exists():
#                     print(f"Theme name '{new_name}' already exists. Skipping installation.")
#                     return None  # Skip this installation
#             elif response == 's':
#                 print(f"Skipping installation of {theme_dir.name}.")
#                 return None  # Skip this installation

#         return theme_dir  # Return the final path for installation

#     def download_and_install(self):
#         """Download and install the theme components."""
#         download_links = self.get_download_links()

#         themes_dir = Path.home() / ".themes"
#         icons_dir = Path.home() / ".icons"
#         shell_dir = Path.home() / ".local/share/gnome-shell/extensions"

#         themes_dir.mkdir(parents=True, exist_ok=True)
#         icons_dir.mkdir(parents=True, exist_ok=True)
#         shell_dir.mkdir(parents=True, exist_ok=True)

#         for theme_type, url in download_links.items():
#             print(f"Downloading {theme_type} from {url}...")
#             response = requests.get(url)
#             response.raise_for_status()  # Raise an error for bad responses

#             # Determine the file extension to handle extraction
#             filename = url.split("/")[-1]
#             filepath = Path.home() / filename
            
#             # Save the file
#             with open(filepath, 'wb') as file:
#                 file.write(response.content)

#             # Extract files based on the file type
#             temp_dir = Path.home() / "temp_extracted"
#             temp_dir.mkdir(parents=True, exist_ok=True)

#             try:
#                 if filename.endswith('.zip'):
#                     with zipfile.ZipFile(filepath, 'r') as zip_ref:
#                         zip_ref.extractall(temp_dir)
#                 elif filename.endswith('.tar.gz'):
#                     with tarfile.open(filepath, 'r:gz') as tar_ref:
#                         tar_ref.extractall(temp_dir)
#                 elif filename.endswith('.tar'):
#                     with tarfile.open(filepath, 'r:') as tar_ref:
#                         tar_ref.extractall(temp_dir)
#                 else:
#                     print(f"Warning: Unsupported file type for {filename}.")
#                     continue
#             except Exception as e:
#                 print(f"Error extracting {filename}: {e}")
#                 continue

#             # Check if the temp_dir contains only one folder
#             extracted_folders = list(temp_dir.iterdir())
#             if len(extracted_folders) == 1 and extracted_folders[0].is_dir():
#                 # If there's only one folder, get that folder's path
#                 main_theme_folder = extracted_folders[0]

#                 # Move valid themes from the main folder to the appropriate directories
#                 for extracted_theme in main_theme_folder.iterdir():
#                     if extracted_theme.is_dir():
#                         # Determine the target directory
#                         target_dir = themes_dir / extracted_theme.name if self.validate_theme(extracted_theme, 'GTK') else \
#                                      icons_dir / extracted_theme.name if self.validate_theme(extracted_theme, 'Icons') else \
#                                      icons_dir / extracted_theme.name if self.validate_theme(extracted_theme, 'Cursors') else \
#                                      shell_dir / extracted_theme.name if self.validate_theme(extracted_theme, 'Shell') else None
                        
#                         if target_dir:
#                             # Handle existing theme paths
#                             final_target_dir = self.handle_existing_theme(target_dir)
#                             if final_target_dir is not None:
#                                 shutil.move(str(extracted_theme), str(final_target_dir))
#                                 print(f"{theme_type} Theme {extracted_theme.name} installed successfully at {final_target_dir}.")
#                         else:
#                             print(f"Warning: {extracted_theme.name} is not a valid theme.")
#             else:
#                 # If there are multiple folders or none, handle them as before
#                 for extracted_theme in temp_dir.iterdir():
#                     if extracted_theme.is_dir():
#                         target_dir = themes_dir / extracted_theme.name if self.validate_theme(extracted_theme, 'GTK') else \
#                                      icons_dir / extracted_theme.name if self.validate_theme(extracted_theme, 'Icons') else \
#                                      icons_dir / extracted_theme.name if self.validate_theme(extracted_theme, 'Cursors') else \
#                                      shell_dir / extracted_theme.name if self.validate_theme(extracted_theme, 'Shell') else None

#                         if target_dir:
#                             final_target_dir = self.handle_existing_theme(target_dir)
#                             if final_target_dir is not None:
#                                 shutil.move(str(extracted_theme), str(final_target_dir))
#                                 print(f"{theme_type} Theme {extracted_theme.name} installed successfully at {final_target_dir}.")
#                         else:
#                             print(f"Warning: {extracted_theme.name} is not a valid theme.")

#             # Clean up
#             shutil.rmtree(temp_dir)  # Remove temporary extraction directory
#             os.remove(filepath)       # Remove the downloaded file

#     def __str__(self):
#         return f"Theme: {self.name}\n" \
#                f"  GTK: {self.gtk_link}\n" \
#                f"  Icons: {self.icon_link}\n" \
#                f"  Cursors: {self.cursor_link}\n" \
#                f"  Shell: {self.shell_link}\n"
