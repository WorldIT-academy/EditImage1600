import customtkinter as ctk

class App_Frame(ctk.CTkFrame):
    def __init__(self, child_master: object, child_width : int, child_height: int, child_fg_color: str, **kwargs):
        ctk.CTkFrame.__init__(
            self, 
            master = child_master, 
            width = child_width , 
            height = child_height,
            fg_color = child_fg_color,
            corner_radius = 0,
            **kwargs
        )
    