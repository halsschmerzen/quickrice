from desktop.quick_themes.theme import Theme

def test_download():
    Numix_Theme = Theme('Numix', 'https://github.com/numixproject/numix-gtk-theme/archive/refs/heads/master.zip',
                        'https://github.com/numixproject/numix-icon-theme-circle/archive/refs/heads/master.zip',
                        'https://github.com/numixproject/numix-cursor-theme/releases/download/v1.2/numix-cursor-1.2.tar',
                        'https://github.com/vinceliuice/Vimix-gtk-themes/archive/refs/heads/master.zip')
    
    Numix_Theme.download_and_install()