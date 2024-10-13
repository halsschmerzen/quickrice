from desktop.detect_desktop import return_desktop
from interactive.create.create_desktop import create_new_rice, read_theme
from interactive.apply.apply_theme import list_available_themes, choose_theme

def banner():

    return '''
                    _     __  
         ___ ___ __(_)___/ /__
        / _ `/ // / / __/  '_/
        \_, /\_,_/_/\__/_/\_\ 
         /_/  ____(_)______   
             / __/ / __/ -_)  
            /_/ /_/\__/\__/   

        quickrice! A simple and quick way to
        change your rice from the CLI.                               
    '''


def display_main():
    print(banner())

    desktop = return_desktop()

    print(f'You are currently on {desktop}. ')

    # Example usage:
    #create_new_rice()
    #print(read_theme('MagicArrow2'))
    
    option = int(input('Choose your option: 1- gen rice 2- apply rice'))

    if option==1:
        create_new_rice()
    elif option == 2:
        choose_theme()


