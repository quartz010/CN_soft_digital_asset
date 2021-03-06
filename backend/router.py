# coding:utf-8
from fileProcing import FileProc
from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
import threading

app = Flask(__name__)
fproc = FileProc()


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello Flask!'
    


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)

        t = threading.Thread(target=fproc.get_info,args=(f,))
        t.start()
        
        return redirect(url_for('upload'))

    return render_template('upload.html')
