from urllib.request import Request
from label_studio.core.utils.params import  get_env
from label_studio.core.utils.io import get_data_dir
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
pdflc = 0
# create projects for pdffilename
BASE_DATA_DIR = get_env('BASE_DATA_DIR', get_data_dir())
print(BASE_DATA_DIR)
def createproject(string1):
    dataa = {'title':string1}
    apiurl = 'http://localhost:8080/api/projects'
    resp = requests.post(apiurl,headers={'Authorization': 'Token 02bde5a7e239bf8707ebd94559e278ff4a9f01fb'},data=dataa)
    axd = resp.json()
    id = str(axd['id'])
    return id
# # uploading converted images from pdf to api
def upload_img_to_api(imgname,uid):
        apiurl = "http://localhost:8080/api/projects/%s/import"%(uid)
        add = uid + '/'+ imgname
        idr0 = r'C:\\Users\\hp\\AppData\\Local\\label-studio\\label-studio\\media\\upload\\2\\'
        idr = r'./images123/%s'%(add)
        # idr = r'./images123/%s'%(imgname)
        try:
            test_file = open(idr,'rb')
            print('hello')
        except:
            #later
            # os.mkdir(idr0)
            test_file = open(idr,'rb')
        Res1 = requests.post(apiurl,headers={'Authorization': 'Token 02bde5a7e239bf8707ebd94559e278ff4a9f01fb'},files={"form_f":test_file})
            # print(Res.headers)
        print(Res1.status_code)
# #image move to destination
def imgmov(imgnmp,uid):
        print('step5')
        ori = r'./%s'%(imgnmp)
        try:
            os.makedirs('./images123/%s'%(uid))
        except:
            print()
        t = r'./images123/%s'%(uid)
        shutil.move(ori,t)
        print('step6')
        upload_img_to_api(imgnmp,uid)
        print("divyam imgmov")
# #pdf into image function
def pdftoimg(string1):
        try:
            print('step2')
            images = convert_from_path('C:\\Users\\hp\\AppData\\Local\\label-studio\\label-studio\\media\\upload\\54\\%s'%(string1))
            print('step3')
            uid = createproject(string1[10:])
            for i in range(len(images)):
                images[i].save('page'+str(i)+'_id'+'.jpg','JPEG')
                movimgvp = 'page'+str(i)+'_id'+'.jpg'
                print('step4')
                imgmov(movimgvp,uid)
            db.insert({'pdfname': string1})
        except:
            print()
def listelem():
    #function to read all files from storing directJory
    listfile = os.listdir('C:\\Users\\hp\\AppData\\Local\\label-studio\\label-studio\\media\\upload\\54\\')
    return listfile
# # mainact work to search name in txt and notfound perform pdf to image task and add value in txt
def mainact(string1):
    #new work____
    User = Query()
    pdfsea = bool(db.search(User.pdfname == string1))
    if(pdfsea):
        print('yes')
    else:
        print('1')
        pdftoimg(string1)
listfile = os.listdir('C:\\Users\\hp\\AppData\\Local\\label-studio\\label-studio\\media\\upload\\54')
a = len(listfile)
for i in range(len(listfile)):
    try:
        lm = listelem()
        string1 = lm[pdflc]
        print(string1)
        mainact(string1)
        pdflc = pdflc + 1
    except:
        print()

ac = "divyam_verma.pdf"
dc = "divyam_verma.jpg"
print(ac[:-4:-1])