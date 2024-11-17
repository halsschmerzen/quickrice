import math

def choose_from_list(options):
    if not options:
        print("The list is empty.")
        return None

    # Determine the number of columns for the grid display
    num_columns = math.ceil(math.sqrt(len(options)))  # You can adjust this logic if desired
    num_rows = math.ceil(len(options) / num_columns)

    print("Please choose an option by entering the corresponding number:")

    # Display the options in a grid format
    for row in range(num_rows):
        for col in range(num_columns):
            index = row * num_columns + col
            if index < len(options):
                # Print each option in the grid
                print(f"{index + 1:2}. {options[index]:<20}", end='  ')  # Adjust spacing as necessary
        print()  # New line after each row

    while True:
        try:
            # Get user input
            choice = int(input("Enter the number of your choice: "))
            
            # Validate the choice
            if 1 <= choice <= len(options):
                selected_option = options[choice - 1]
                print(f"You selected: {selected_option}")
                return selected_option
            else:
                print("Invalid choice. Please try again.")
        
        except ValueError:
            print("Please enter a valid number.")