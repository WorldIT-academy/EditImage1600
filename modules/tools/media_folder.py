"""
    This module writed for creating directoris with name 'media'
"""
from os.path import abspath, exists, join 
import os
import colorama

colorama.init()

GREEN = colorama.Fore.GREEN
YELLOW = colorama.Fore.YELLOW
RESET_STYLES = colorama.Style.RESET_ALL
def create_media_folder():
    """
        Створює папку media  в основній директорії програми edit image
        Приклад застосування: 
        >>> create_media_folder()
    """
    # записуємо у змінну path_media абсолютний шлях у форматі str до папки media
    path_media = abspath(join(__file__, "..", "..", "..", "media"))
    try:
        for dir in ['downloads', 'edits']:
            if not exists(join(path_media, dir)):
                print(f'\n{YELLOW}Created media folder {GREEN + dir.upper() + YELLOW}...!{RESET_STYLES}\n')
            os.makedirs(join(path_media, dir), exist_ok= True)
    except Exception as exception:
        print(f'{colorama.Fore.RED}Error created media folder: {str(exception)}!{colorama.Style.RESET_ALL}')
    

    

