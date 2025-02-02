from os.path import abspath, join

def create_path(filename: str):
    path_list = filename.split('/')
    path_modules = abspath(join(__file__, "..", "..", ".."))
    for path in path_list:
        path_modules = join(path_modules, path)
    print()
    print(f'Шлях до файлу: {path_modules}')
    return path_modules
    

