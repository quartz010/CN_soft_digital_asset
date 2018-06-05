# coding:utf-8
import hashlib
import json
import time
import requests


import urllib
import os
import base64

TIMEOUT = 3

class FileProc(object):
    
    def __init__(self, file=None):
        self.file = file
        self.file_info = {
            'name' : '',
            'hash' : '',
            'more' : ''
        }

    def set_file(self, file):
        self.file = file

    def __name(self):
        self.file_info['name'] = self.file.filename
    
    def __hash(self):
        hs = hashlib.sha1()
        hs.update(self.file.read())
        self.file_info['hash'] = hs.hexdigest()
        self.file_info['more'] = [1,1,12,6,323,4]

    def get_info(self, file=None):
        self.file = file
        self.__name()
        self.__hash()

        print(json.dumps(self.file_info, sort_keys=True, indent=4, separators=(',', ': ')))



class RemoteProc(object):
    
    def __init__(self, file = None):
        self.r_url = {
            'ocr':'https://api.ai.qq.com/fcgi-bin/ocr/ocr_generalocr'
        }

    def picOCR(self, file = None):
        def encodePic():

            with open('C:\\Users\\R4y\\Desktop\\a.png', 'rb') as f:
                data = base64.b64encode(f.read())
                return data

        self.__httpReq(encodePic())

    def __httpReq(self, image):
  
        def genSignString(parser):
            uri_str = ''
            for key in sorted(parser.keys()):
                if key == 'app_key':
                    continue
                uri_str += "%s=%s&" % (key, urllib.parse.quote(str(parser[key]), safe = ''))
            sign_str = uri_str + 'app_key=' + parser['app_key']

            hash_md5 = hashlib.md5(sign_str.encode('utf8'))
            return hash_md5.hexdigest().upper()

        def req():
            return requests.post( self.r_url['ocr'],data=keywords, json=None, timeout=TIMEOUT)

        keywords = {
            "app_id": "",
            "time_stamp": "",
            'nonce_str': '',
            'sign': '',
            'image': ''
        }
        time_stamp = int(time.time())
        keywords['time_stamp'] = time_stamp
        keywords['nonce_str'] = time_stamp
        keywords['app_key'] = 'nZ6D4DlLUIkczG92'
        keywords['app_id'] = '1106953556'
        
        keywords['image'] = image

        keywords['sign'] = genSignString(keywords)
        try:
            res  = req()
            print(res.text)
        except requests.exceptions.ConnectTimeout:
            
            print('[-] Connect Timeout!')
            return False

        

        
app_key = '1106953556'
<<<<<<< HEAD
app_id = ''
=======
app_id = 'nZ6D4DlLUIkczG92'
>>>>>>> 422a917935b9ab2b66b0f1aab7b1f5869608c2dd

a = RemoteProc()
a.picOCR()

