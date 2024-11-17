#!/usr/bin/env python3

import argparse
import re
from quickrice.interactive.main_menu import display_main
from quickrice.interactive.create.create_desktop import create_new_rice
from quickrice.interactive.apply.apply_theme import apply_theme_by_name, list_available_themes
from quickrice.desktop.detect_desktop import return_desktop
from quickrice.desktop.extensions.check_system import detect_package_manager, collect_necessary_packages
from quickrice.desktop.extensions.download_extensions import check_package_installed, install_necessary_packages

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='quickrice - A simple CLI tool to manage your desktop themes.')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # 'generate' command
    parser_generate = subparsers.add_parser('generate', help='Generate a new rice (theme)')

    # 'apply' command
    parser_apply = subparsers.add_parser('apply', help='Apply an existing rice (theme)')
    parser_apply.add_argument('theme', nargs='?', help='Name of the theme to apply')
    
    # 'list' command
    
    parser_list = subparsers.add_parser('list', help='List available themes')

    args = parser.parse_args()

    # Check for necessary packages
    package_manager, install_command = detect_package_manager()
    necessary_packages = collect_necessary_packages(package_manager)
    packages_to_install = []

    for pkg in necessary_packages:
        if not check_package_installed(pkg, package_manager):
            packages_to_install.append(pkg)

    if packages_to_install:
        print(f"Installing necessary packages: {packages_to_install}")
        install_necessary_packages(packages_to_install)
    else:
        print("All necessary packages are already installed.")

    # Execute the command based on user input
    if args.command == 'generate':
        create_new_rice()
    elif args.command == 'apply':
        if args.theme:
            apply_theme_by_name(args.theme)
        else:
            print('Please specify a theme name to apply.')
            parser_apply.print_help()
    elif args.command == 'list':
        themes, _ = list_available_themes()
        if themes:
            print('Available Themes:')
            for idx, theme in enumerate(themes, start=1):
                print(f'{idx}. {theme}')
        else:
            print('No themes found.')
    
    else:
        display_main()

if __name__ == '__main__':
    main()