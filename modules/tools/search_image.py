import tkinter.filedialog as filedialog

def get_file_path(parent: object):
    
    list_path_files = filedialog.askopenfilenames(
        title= 'Get File Path',
        initialdir= '/',
        filetypes= [('file image', ['*.png','*.jpg', '*.bmp', '*.ico', '*.svg', '*.jpeg'])],
        parent= parent
        
    )
    print()
    for path in list_path_files:
        print(f'Selected file: {path.split('/')[-1]}')
    print()
    
