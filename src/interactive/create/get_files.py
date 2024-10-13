import os

class ThemeOptions:
    def __init__(self, theme_dirs):
        self.theme_dirs = theme_dirs
    
    def get_available_themes(self, directories, validation_func=None):
        """Fetches available themes from the specified directories and validates them."""
        themes = set()
        for directory in directories:
            if os.path.exists(directory):
                for theme in next(os.walk(directory))[1]:  # Get directory names
                    theme_path = os.path.join(directory, theme)
                    if validation_func is None or validation_func(theme_path):
                        themes.add(theme)
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

