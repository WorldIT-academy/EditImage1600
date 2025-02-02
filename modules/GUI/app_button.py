r"""
    ### У цьому файлі вказана інструкція (клас AppButton), яка створює кнопку у графічному інтерфейсу додатку 
    
    Приклад використання:
    
    ```python
        self.BUTTON_SEARCH = AppButton(
            ch_master = self.VERTICAL_MENU,
            icon_name = "explorer.png",
            size = self.VERTICAL_MENU._current_width * 0.5
        )
    ```
    [Посилання на GitHub ресурси файлу app_button.py](https://github.com/WorldIT-academy/EditImage1600/blob/main/modules/GUI/app_button.py)
    
"""
import PIL.Image
import customtkinter as ctk
from os.path import abspath, join
import colorama
from ..tools.create_path import create_path

colorama.init(autoreset= True)

class AppButton(ctk.CTkButton):
    '''
        Інструкція (клас) що завантажує зображення, за вказаним ім'ям іконки у папці static/icon
        і додає до параметру => image у конструкторі CTkButton. Та створює кнопку у графічному інтерфейсі застосунку
        
        #### Конструктор AppButton: 
    
            - :mod:`ch_master`: батьківський елемент, до якого потрібно додати кнопку;
            - :mod:`icon_name`: назва зображення з папки static/icon;
            - :mod:`size`: розмір кнопки (в пікселах);
            - :mod:`**kwargs`: додаткові аргументи для кнопки (наприклад, command, font, relief).   
        
        #### Властивості класу AppButton: 
            - :mod:`ICON_NAME`: назва зображення з папки static/icon;
            - :mod:`SIZE`: розмір кнопки (в пікселах);
            
        #### Методи класу AppButton: 
            - :mod:`load_image()`: визначає зображення кнопки з використанням PIL.Image,
              завантажує зображення з папки static/icon і зберігає його у вигляді CTkImage.
            - :mod:`load_image()`: повертає зображення кнопки або None, якщо зображення не знайдено.
    '''

    def __init__(
            self, 
            ch_master: object, 
            icon_name: str= None, 
            size: float = 0, 
            function: object = None, 
            text_button: str = "", 
            **kwargs
        ):
        '''
            Інструкція (клас) що завантажує зображення, за вказаним ім'ям іконки у папці static/icon
            і додає до параметру => image у конструкторі CTkButton. Та створює кнопку у графічному інтерфейсі застосунку

            #### Конструктор AppButton: ####

                - :mod:`ch_master`: батьківський елемент, до якого потрібно додати кнопку;
                - :mod:`icon_name`: назва зображення з папки static/icon;
                - :mod:`size`: розмір кнопки (в пікселах);
                - :mod:`**kwargs`: додаткові аргументи для кнопки (наприклад, command, font, relief).   

            #### Властивості класу AppButton: ####
                - :mod:`ICON_NAME`: назва зображення з папки static/icon;
                - :mod:`SIZE`: розмір кнопки (в пікселах);

            #### Методи класу AppButton: ####
                - :mod:`load_image()`: визначає зображення кнопки з використанням PIL.Image,
                  завантажує зображення з папки static/icon і зберігає його у вигляді CTkImage.
                - :mod:`load_image()`: повертає зображення кнопки або None, якщо зображення не знайдено.
        '''

        self.ICON_NAME = icon_name
        self.SIZE = (int(size), int(size))
        # self.FONT = ctk.FontManager.load_font(font_path= create_path(filename= 'static/font/RobotoMono-Bold.ttf'))
        
        ctk.CTkButton.__init__(
            self, 
            master= ch_master,
            image= self.load_image(),
            text = text_button,
            width = int(size),
            height = int(size),
            fg_color= ch_master._fg_color,
            hover_color= '#373535',
            command= function,
            corner_radius= 10,
            
            font= ctk.CTkFont(family= create_path(filename= 'static/font/Jomolhari-Regular.ttf'), size= 12),
            
            **kwargs
        )
        
    def load_image(self) -> ctk.CTkImage | None:
        '''
            Завантажує зображення з використанням PIL.Image та повертає його у вигляді CTkImage.
        '''
        try:
            PATH = abspath(join(__file__, "..", "..", "..", "static", "icon", self.ICON_NAME))
            return ctk.CTkImage(
                light_image= PIL.Image.open(fp= PATH),
                size= self.SIZE
            )
        except Exception as exception:
            print(f'{colorama.Fore.RED}Error load image: {str(exception)}!')  # Виводить помилку у консоль, а не в графічному інтерфейсі.
            return None