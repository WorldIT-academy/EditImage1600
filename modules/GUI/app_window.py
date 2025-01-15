import customtkinter as ctk
from ..json.read_json import read_json
from ..tools import create_media_folder
from .app_frames import App_Frame 
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
        #
        self.HEADER = App_Frame(child_master = self, 
                                child_width = self.WIDTH, 
                                child_height = self.HEIGHT * 0.05, 
                                child_fg_color = "#181818"
        )
        self.HEADER.grid(row = 0, column = 0)

        self.CONTENT = App_Frame(child_master= self,
                                child_width= self.WIDTH,
                                child_height= self.HEIGHT * 0.95,
                                child_fg_color= "#1f1f1f"
        )
        self.CONTENT.grid(row= 1, column= 0, pady= 1)
        
        
#
app = App()
