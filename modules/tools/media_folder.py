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
    """
    # записуємо у змінну path_media абсолютний шлях у форматі str до папки media
    path_media = abspath(join(__file__, "..", "..", "..", "media"))
    try:
        for dir in ['downloads', 'edits']:
            # умова яка перевіряє наявність папки downloads або edits
            if not exists(join(path_media, dir)):
                # Створюємо папку за вказаним шляхом, та забороняємо виводити помилки задопомогою параметру exist_ok
                os.makedirs(join(path_media, dir), exist_ok= True)
                print(f'\n{YELLOW}Created media folder {GREEN + dir.upper() + YELLOW}...!{RESET_STYLES}\n')
    except Exception as exception:
        print(f'{colorama.Fore.RED}Error created media folder: {str(exception)}!{colorama.Style.RESET_ALL}')
    

    

