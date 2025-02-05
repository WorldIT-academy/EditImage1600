import customtkinter as ctk
from ..json.read_json import read_json
from ..tools import create_media_folder, get_file_path
from .app_frames import App_Frame 
from .app_button import AppButton

# Розробляємо інструкцію App, для створення віконого десктопного додатку за цією інструкцію 
class App(ctk.CTk):
    def __init__(self):
        # Створюємо локальну змінну з типом даних словник, куди записуємо усі дані із файла config.json
        data = read_json(filename= 'config.json')

        
        ctk.CTk.__init__(self, fg_color = data["app_fg_color"])
        
        create_media_folder()
        
        # Створюємо властивість класу Аpp (глобальна зміна класа App), 
        # задаємо розмір екрану додатака, по ширини, у відсотковому відношенені 
        # 80% до ширини екрану компьютера
        self.WIDTH = int(self.winfo_screenwidth() * data['app_width'])
        # задаємо розмір екрану додатака, по висоті, у відсотковому відношенені 
        # 80% до висоти екрану компьютера
        self.HEIGHT = int(self.winfo_screenheight() * data['app_height'])
        # створюємо екран застосунку за вказаними величинами (WIDTH, HEIGHT), в координатах x = 0, y = 0 
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        # Задаємо заголовок нашому застосунку 
        self.title(data['title'])
        self.resizable(False, False)
        #
        self.HEADER = App_Frame(
            child_master = self, 
            child_width = self.WIDTH, 
            child_height = self.HEIGHT * 0.051, 
            child_fg_color = "#181818"
        )
        self.HEADER.place(x = 0, y = 0)
        

        self.CONTENT = App_Frame(
            child_master= self,
            child_width= self.WIDTH,
            child_height= self.HEIGHT * 0.95,
            child_fg_color= "#ffffff"
        )
        self.CONTENT.place(x = 0, y = self.HEIGHT * 0.05 + 1)
        #
        self.VERTICAL_MENU = App_Frame(
            child_master = self.CONTENT,
            child_width = self.CONTENT._current_width * 0.05,
            child_height = self.CONTENT._current_height,
            child_fg_color = '#181818'
        )
        self.VERTICAL_MENU.place(x = 0, y = 0)
        
        
        self.EXPLORER = App_Frame(
            child_master= self.CONTENT,
            child_width= self.CONTENT._current_width * 0.15,
            child_height= self.CONTENT._current_height,
            child_fg_color = "#181818"
        )
        self.EXPLORER.place(x = self.CONTENT._current_width * 0.05 + 1 , y= 0)
        #
        self.DASHBOARD = App_Frame(
            child_master= self.CONTENT,
            child_width= self.CONTENT._current_width * 0.8,
            child_height= self.CONTENT._current_height,
            child_fg_color= "#ffffff"                
        )
        self.DASHBOARD.place(x = self.CONTENT._current_width * 0.1999 + 1, y = 0)
        #
        self.HEADER_DASHBOARD = App_Frame(
            child_master = self.DASHBOARD,
            child_width = self.DASHBOARD._current_width,
            child_height = self.DASHBOARD._current_height * 0.03,
            child_fg_color = '#181818'                    
        )
        self.HEADER_DASHBOARD.place(x = 0, y = 0)   
        #
        self.CONTENT_DASHBOARD = App_Frame(
            child_master= self.DASHBOARD,
            child_width= self.DASHBOARD._current_width,
            child_height= self.DASHBOARD._current_height * 0.97,
            child_fg_color= "#1f1f1f"
        )
        self.CONTENT_DASHBOARD.place(x=0, y=self.DASHBOARD._current_height * 0.03)

        self.BUTTON_SEARCH = AppButton(
            ch_master = self.VERTICAL_MENU,
            icon_name = "explorer.png",
            size = self.VERTICAL_MENU._current_width * 0.5,
            function= lambda: get_file_path(parent= self, button_parent= self.EXPLORER, dashboard= self.CONTENT_DASHBOARD)
        )
        self.BUTTON_SEARCH.place(x = 20, y = 20)
        
        
app = App()
