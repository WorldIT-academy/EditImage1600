import tkinter.filedialog as filedialog
from ..gui.app_button import AppButton
from tkinter import Y, BOTH, LEFT, TOP

def get_file_path(parent: object, button_parent : object):
    
    list_path_files = filedialog.askopenfilenames(
        title= 'Get File Path',
        initialdir= '/',
        filetypes= [('file image', ['*.png','*.jpg', '*.bmp', '*.ico', '*.svg', '*.jpeg'])],
        parent= parent
        
    )
    print()
    for path in list_path_files:
        print(f'Selected file: {path.split('/')[-1]}')
        button = AppButton(
            ch_master = button_parent,
            text_button = path.split('/')[-1]
        )
        button.pack(
            pady = 20,
            padx = 20,
            anchor = 'w'
            # expand = True, 
            # fill = BOTH, 
            # side = LEFT
        )
        
        button_parent.pack_propagate(False)
    print() 
    
