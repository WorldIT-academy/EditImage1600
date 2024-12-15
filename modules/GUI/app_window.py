import customtkinter as ctk

from ..json.read_json import read_json

class App(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)
        
        data = read_json(filename= 'config.json')
        
        self.WIDTH = int(self.winfo_screenwidth() * data['app_width'])
        self.HEIGHT = int(self.winfo_screenheight() * data['app_height'])
        
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.title(data['title'])

app = App()
