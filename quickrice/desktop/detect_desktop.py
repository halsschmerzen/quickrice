import os
from quickrice.desktop.desktops import GnomeTheme, CinnamonTheme

def return_desktop():

    current_desktop = os.getenv('XDG_SESSION_DESKTOP')

    if current_desktop:
        return current_desktop.lower()
    
    return 'Could not find current Desktop. Perhaps you are not on Linux?'

def detect_desktop_class():
    desktop = return_desktop()

    

