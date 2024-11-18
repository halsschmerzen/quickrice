import os
import json
import curses
import re
from desktop.detect_desktop import return_desktop

config_dir = os.path.expanduser('~/.config/quickrice/rices')
current_desktop = return_desktop().lower()
folders = {
        "gnome": [r'gnome.*|ubuntu'],
        "cinnamon": [r'cinnamon'],
        "xfce": [r'xfce']
    }
def list_themes(): 
    themes = []
    if current_desktop in folders:
        for pattern in folders[current_desktop]:
            for root, dirs, files in os.walk(config_dir):
                if re.search(pattern, root):
                    for file in files:
                        if file.endswith('.json'):
                            themes.append(file)
    return themes


def delete_theme_by_name(theme_name):
    
    for desktop, patterns in folders.items():
        for pattern in patterns:
            if re.match(pattern, current_desktop):
                desktop_dir = os.path.join(config_dir, desktop)
                break
        
    if desktop_dir is None:
        print('Invalid theme name!!')
            
        
    theme_file = os.path.join(desktop_dir, theme_name + '.json')
    if os.path.exists(theme_file):
        os.remove(theme_file)
        print(f'Theme {theme_name} deleted succesfully')
    else:
        print(f'Invalid theme name!')
    
    

def delete_themes(selected_themes):
    for theme in selected_themes:
        theme_path = os.path.join(config_dir, current_desktop, theme)
        if os.path.exists(theme_path):
            os.remove(theme_path)
            print(f"Deleted theme: {theme}")
        else:
            print(f"Theme not found: {theme}")

def curses_menu(stdscr, themes):
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    selected = [False] * len(themes)
    current_row = 0
    
    while True:
        stdscr.clear()
        h, w = stdscr.getmaxyx()
        
        for idx, theme in enumerate(themes):
            x = w//2 - len(theme)//2
            y = h//2 - len(themes)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, theme)
                stdscr.attroff(curses.color_pair(1))
                stdscr.addstr(y, x + len(theme) + 2, "<--------")
            else:
                stdscr.addstr(y, x, theme)
            
            if selected[idx]:
                stdscr.addstr(y, x - 6, "[X]")
            
        stdscr.addstr(h-2,w//2-len("ESC to leave (might take a second, curses is slow)")//2, "ESC to leave (might take a second, curses is slow)")
        stdscr.refresh()
        
        key = stdscr.getch()
        
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(themes) - 1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            selected[current_row] = not selected[current_row]
        elif key == 27:  # ESC
            if any(selected):
                stdscr.clear()
                stdscr.addstr(h//2, w//2 - 20, "Are you sure you want to delete the selected themens? [y/n]")
                stdscr.refresh()
                confirm_key = stdscr.getch()
                
                if confirm_key in [ord('y'), ord('Y')]:
                    return [theme for idx, theme in enumerate(themes) if selected[idx]]
                else:
                    return[]
            else:
                return []

def delete_rice():
    themes = list_themes()
    if not themes:
        print("No themes available for deletion.")
        return
    
    selected_themes = curses.wrapper(curses_menu, themes)
    
    if selected_themes:
        delete_themes(selected_themes)
    else:
        print("No themes selected for deletion.")
