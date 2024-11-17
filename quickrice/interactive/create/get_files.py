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
        """Displays a sorted list of themes in grid format and allows the user to choose one by number."""
        if not theme_list:
            print(f"No {theme_type} themes available.")
            return None

        # Sort the list alphabetically
        theme_list = sorted(theme_list)
        print(f"\nAvailable {theme_type} themes:")

        # Define the number of columns
        num_columns = 3
        num_items = len(theme_list)
        num_rows = (num_items + num_columns - 1) // num_columns  # Ceiling division

        # Create rows for the grid
        grid = []
        for row_idx in range(num_rows):
            row = []
            for col_idx in range(num_columns):
                index = row_idx + num_rows * col_idx
                if index < num_items:
                    theme = theme_list[index]
                    idx = index + 1
                    row.append(f"{idx}: {theme}")
                else:
                    row.append('')
            grid.append(row)

        # Calculate column width for alignment
        col_width = max(len(item) for row in grid for item in row if item) + 2

        # Print the grid
        for row in grid:
            print("".join(item.ljust(col_width) for item in row))

        while True:
            try:
                choice = int(input(f"\nEnter the number of the {theme_type} theme you want to select: "))
                if 1 <= choice <= len(theme_list):
                    return theme_list[choice - 1]
                else:
                    print(f"Please choose a number between 1 and {len(theme_list)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

