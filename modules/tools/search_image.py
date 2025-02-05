import tkinter.filedialog as filedialog
from ..gui.app_button import AppButton
from tkinter import Y, BOTH, LEFT, TOP
import customtkinter as ctk
from ..gui.app_image import show_image


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
            function= lambda: show_image(parent= dashboard, path_image= path)
        )
        button.pack(pady = 20, padx = 20, anchor = 'w')
    print() 
    
