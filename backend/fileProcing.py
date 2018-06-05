# coding:utf-8
import hashlib
import json

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

    def get_info(self):
        self.__name()
        self.__hash()

        print(json.dumps(self.file_info, sort_keys=True, indent=4, separators=(',', ': ')))

        

