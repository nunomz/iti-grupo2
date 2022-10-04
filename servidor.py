from crypt import methods
from flask import Flask, json, request, jsonify, send_from_directory, send_file, current_app, render_template
import os
import urllib.request
import shutil
import random
from werkzeug.utils import secure_filename
 
app = Flask(__name__)
 
app.secret_key = "caircocoders-ednalan"
 
MUSIC_FOLDER = 'music'
UPLOAD_FOLDER = 'uploads' 
ZIP_FOLDER = 'zips'
app.config['MUSIC_FOLDER'] = MUSIC_FOLDER
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ZIP_FOLDER'] = ZIP_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
 
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
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

#
#

@app.route('/', methods=['POST'])
def upload_file():
    # check if the post request has the file part
    if 'file' not in request.files:
        resp = jsonify({'message' : 'No file part in the request'})
        resp.status_code = 400
        return resp                                                 
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return Homepage
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename) 
        #create folder and save file to it
        foldername = os.path.splitext(filename)[0] #foldername = filename without extension
        path = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], foldername)
        os.mkdir(path)
        file.save(os.path.join(path, filename))
        #adds random songs to folder
        input_dir= os.path.join(current_app.root_path, app.config['MUSIC_FOLDER'])
        file_list = get_file_list(input_dir) 
        random_files = get_random_files(file_list, 10)
        copy_files(random_files, input_dir, path)
        success = True
        return '''
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        '''
    

@app.route('/download/<path:filename>', methods=['GET'])
def downloadfile(filename):
    dir_name = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'], filename) #sets folder to zip
    output_filename = os.path.join(current_app.root_path, app.config['ZIP_FOLDER'], 'zip_'+filename) #sets desired location and name for zip file
    shutil.make_archive(output_filename, 'zip', dir_name) #zippity zoppity
    final_filename = os.path.join(current_app.root_path, app.config['ZIP_FOLDER'], 'zip_'+filename+'.zip') #zip file
    return send_file(final_filename) #sends zip file

if __name__ == '__main__':
    app.run(debug=True)