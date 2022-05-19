from tinydb import TinyDB, Query
db = TinyDB('counter.json')

import os

string1 ='counternull'    
User = Query()
pdfsea = bool(db.search(User.pdfname == string1))
if(pdfsea):
    os.system('python3 pdf_to_image_project.py')
else:
    print('g')
db.insert({'pdfname': 'counternull'})