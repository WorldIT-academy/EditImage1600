import tkinter.filedialog as filedialog
from ..gui.app_button import AppButton
from tkinter import Y, BOTH, LEFT, TOP
import customtkinter as ctk
from ..gui.app_image import ImageLabel


list_images = []

def show_image(button_name: str, frame: ctk.CTkFrame):
    list_frame = frame.winfo_children()
    for child in list_frame:
        if isinstance(child, ImageLabel):
            child.pack_forget()

    for image in list_images:
        if image.PATH_IMAGE.split('/')[-1] == button_name:
            image.pack(anchor = "center")
            
def get_file_path(parent: ctk.CTk, button_parent: ctk.CTkScrollableFrame | ctk.CTkFrame, dashboard: ctk.CTkFrame):
    r'''
        Визначає шлях до вибраного файлу зображення і створює кнопку з вибраним ім'ям файла.
        
        #### Параметри: ####
        
            - :mod:`parent` (СTk): батьківський елемент, до якого потрібно додати кнопку;
            - :mod:`button_parent` (CTkScrollableFrame | CTkFrame): фрейм у додатку до якого додаємо кнопки з назвами зображень
    '''
    
    list_path_files = filedialog.askopenfilenames(
        title= 'Get File Path',
        initialdir= '/',
        filetypes= [('file image', ['*.png','*.jpg', '*.bmp', '*.ico', '*.svg', '*.jpeg'])],
        parent= parent
        
    )
    print()
    for path in list_path_files:
        # print(f'Selected file: {path.split('/')[-1]}')
        print(f'Selected file: {path}')
        
        button = AppButton(
            ch_master = button_parent,
            text_button = path.split('/')[-1],
            function = lambda name_image = path.split('/')[-1]: show_image(button_name = name_image, frame = dashboard)
            # function= lambda: s
            # how_image(parent= dashboard, path_image= path)
        )
        button.pack(pady = 20, padx = 20, anchor = 'w')
        image = ImageLabel(
            ch_master = dashboard,
            path_image = path   
        )
        list_images.append(image)
    print() 
    
