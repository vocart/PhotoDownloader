import shutil
import os
import fnmatch

source = 'I:/DCIM/100MSDCF'
destination = 'E:/fotki 2020/1. SELEKCJA ZDJĘĆ/Nowe zdjęcia'

try:
    os.mkdir('E:/fotki 2020/1. SELEKCJA ZDJĘĆ/Nowe zdjęcia')
except FileExistsError:
    pass

try:
    os.mkdir('E:/fotki 2020/1. SELEKCJA ZDJĘĆ/Nowe zdjęcia/raw')
except FileExistsError:
    pass

files = os.listdir(source)
rawPattern = '*.ARW'

for photo in files:
    if fnmatch.fnmatch(photo, rawPattern):
        shutil.move('{}/{}'.format(source, photo), '{}/raw/{}'.format(destination, photo))
    else:
        shutil.move('{}/{}'.format(source, photo), '{}/{}'.format(destination, photo))
