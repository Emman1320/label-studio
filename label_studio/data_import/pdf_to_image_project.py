from urllib.request import Request
from numpy import uint
import tinydb
import json
import imp
import re
import string
from pdf2image import convert_from_path
import os
from pickletools import string1
import shutil
from regex import R
import re
from wsgiref import headers
import requests
from trafaret import Null
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
import json
from tinydb import TinyDB, Query
db = TinyDB('db.json')
dbc = TinyDB('counter.json')

pdflc = 0



# create projects for pdffilename

def createproject(string1):
    dataa = {'title':string1}
    apiurl = 'http://localhost:8080/api/projects'
    
    resp = requests.post(apiurl,headers={'Authorization': 'Token 6173aede29415455c436c8f71a45edb685c40987'},data=dataa)
    axd = resp.json()
    id = str(axd['id'])
    return id
   


# # uploading converted images from pdf to api

def upload_img_to_api(imgname,uid):
	
        apiurl = "http://localhost:8080/api/projects/%s/import"%(uid)

        idrr= uid +'/'+imgname
        idr0 = r'/home/divyam/.local/share/label-studio/media/upload/1/'
        idr = r'./images123/%s'%(idrr)
        test_file = open(idr,'rb')
        print('step5')
        Res1 = requests.post(apiurl,headers={'Authorization': 'Token 6173aede29415455c436c8f71a45edb685c40987'},files={"form_f":test_file})
            # print(Res.headers)
        print(Res1.status_code)	

# #image move to destination

def imgmov(imgnmp,uid):
        ori = r'./%s'%(imgnmp)
        try:
            os.makedirs('./images123/%s'%(uid))
        except:
            print()
        t = r'./images123/%s'%(uid)

        
        shutil.move(ori,t)
        
        upload_img_to_api(imgnmp,uid)



# #pdf into image function

def pdftoimg(string1,foldr_name):
        try:
            ac = foldr_name+'/'+string1
            print(ac)
            images = convert_from_path('/home/divyam/.local/share/label-studio/media/upload/%s'%(ac))
            proj_counter = 0
            # uid = createproject(string1[10:])
            
            for i in range(len(images)):
                images[i].save('page'+str(i)+'_id'+'.jpg','JPEG')
                movimgvp = 'page'+str(i)+'_id'+'.jpg'
                if proj_counter==0:
                    uid = createproject(string1[10:])
                    proj_counter = 1
                else:
                    print()
                imgmov(movimgvp,uid)
            db.insert({'pdfname': string1})
            


        except:
            print()         

        

def listelem(foldr_name):
	#function to read all files from storing directory
	listfile = os.listdir('/home/divyam/.local/share/label-studio/media/upload/%s/'%(foldr_name))
	
	return listfile






# # mainact work to search name in txt and notfound perform pdf to image task and add value in txt
def mainact(string1,foldr_name):
    #new work____
    User = Query()
    pdfsea = bool(db.search(User.pdfname == string1))
    if(pdfsea):

        print('t')
    else:
        print('step2')
        pdftoimg(string1,foldr_name)

    
        

listfile1 = os.listdir('/home/divyam/.local/share/label-studio/media/upload/')

dbc.update({'pdfname': 'run'})
for i in range(len(listfile1)):
    foldr_name = listfile1[i]
    lenin= listelem(foldr_name)
    print(foldr_name)
    for i in range(len(lenin)):
        try:
            lm = listelem(foldr_name)
            string1 = lm[pdflc]
            print(string1)
            mainact(string1,foldr_name)
            pdflc = pdflc + 1              
        except:
            print()

dbc.insert({'pdfname': 'counternull'})

# b=  os.listdir('/home/divyam/.local/share/label-studio/media/upload/')
# print(b)
# print(len(b))
# b,c = os.path.splitext('./codecov.yml')
# print(c)















		
