r'''
    У модулі створено функцію ``read_json``, яка читає будь який файл з розширенням json
    
    та повертає значення з типом даних словник ``(dict)``.
'''

import json 
import os 

def read_json(filename: str) -> dict:
    r'''
        :mod:`Читає` дані із ``json`` файлів та повертає значення з типом даних dict.

        Приклад застосування: 
        >>> data_json = read_json(filename= 'test.json')
    '''
    file_path = os.path.abspath(__file__ + "/../../../static/json/" + filename)
    with open(file_path, 'r') as file:
        return json.load(file)
    