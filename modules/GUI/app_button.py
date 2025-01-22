import PIL.Image
import customtkinter as ctk
from os.path import abspath, join
import PIL

class AppButton(ctk.CTkButton):
    def __init__(self, ch_master: object, icon_name: str, size: float,**kwargs):
        
        self.ICON_NAME = icon_name
        self.SIZE = (int(size), int(size))
        
        ctk.CTkButton.__init__(
            self, 
            master= ch_master,
            image= self.load_image(),
            text = "",
            width = int(size),
            height = int(size),
            fg_color= ch_master._fg_color,
            hover_color= '#373535',
            **kwargs
        )
        
    def load_image(self):
        try:
            PATH = abspath(join(__file__, "..", "..", "..", "static", "icon", self.ICON_NAME))
            return ctk.CTkImage(
                light_image= PIL.Image.open(fp= PATH),
                size= self.SIZE
            )
        except:
            return None