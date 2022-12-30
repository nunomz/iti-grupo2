from crypt import methods
from flask import Flask, json, request, jsonify, send_from_directory, send_file, current_app, render_template
import os
import shutil
import random
import logging
from werkzeug.utils import secure_filename
from flask_cors import CORS
#import memory_profiler as mp   # <----

logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - "
                      "%(name)s:%(lineno)d [-] %(funcName)s- %(message)s")
logger.setLevel(logging.INFO)

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)
 
app.secret_key = "caircocoders-ednalan"
 
MUSIC_FOLDER = 'music'
UPLOAD_FOLDER = 'uploads' 
ZIP_FOLDER = 'zips'
app.config['MUSIC_FOLDER'] = MUSIC_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ZIP_FOLDER'] = ZIP_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp3', 'mp4', 'wav'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_file_list(input_dir):
    return [file for file in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, file))]

def get_random_files(file_list, N):
    return random.sample(file_list, N)

def copy_files(random_files, input_dir, output_dir):
    for file in random_files:
        shutil.copy(os.path.join(input_dir, file), output_dir)

#o primeiro nao interessa nao sei porque

@app.route('/')
def main():
    return render_template('home.html')

# @app.route('/upload')
# def upload_main():
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     <form method=post enctype=multipart/form-data>
#       <input type=file name=file>
#       <input type=submit value=Upload>
#     </form>
#     <p> Allowed extensions are: txt, pdf, png, jpg, jpeg, gif, mp3, mp4, wav</p>
#     '''

#
#

@app.route('/upload', methods=['POST'])
#@mp.profile
def upload_file():
    print(request)
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        resp = jsonify({'message' : 'No selected file'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename) 
        #create folder and save file to it
        foldername = os.path.splitext(filename)[0] #foldername = filename without extension
        path = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], foldername)
        if os.path.exists(path):
            resp = jsonify({'message' : 'File already exists'})
            resp.status_code = 400
            return resp
        os.mkdir(path)
        file.save(os.path.join(path, filename))
        #adds random songs to folder
        input_dir= os.path.join(current_app.root_path, app.config['MUSIC_FOLDER'])
        file_list = get_file_list(input_dir) 
        random_files = get_random_files(file_list, 1)
        copy_files(random_files, input_dir, path)
        #success = True
        return render_template('success.html')
    
@app.route('/list_files/', methods=['GET'])
def getlogs():
    file_list = os.listdir('uploads')
    return jsonify(file_list)

@app.route('/download/')
def logs():
    filenames = os.listdir('/uploads')
    print(filenames)
    return render_template('logs.html', files=filenames)

@app.route('/download/<path:filename>', methods=['GET'])
#@mp.profile
def downloadfile(filename):
    dir_name = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], filename) #sets folder to zip
    output_filename = os.path.join(current_app.root_path, app.config['ZIP_FOLDER'], 'zip_'+filename) #sets desired location and name for zip file
    shutil.make_archive(output_filename, 'zip', dir_name) #zip
    final_filename = os.path.join(current_app.root_path, app.config['ZIP_FOLDER'], 'zip_'+filename+'.zip') #zip file
    return send_file(final_filename) #sends zip file

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')