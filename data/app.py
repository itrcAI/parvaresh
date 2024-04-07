from flask import Flask, render_template, request
import os
import pandas as pd

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    # Check if the file is empty
    if file.filename == '':
        return "No selected file"
    
    if not allowed_file(file.filename):
        return "File type not allowed"
    
    upload_dir = request.form['directory']
    upload_path = os.path.join(app.config['UPLOAD_FOLDER'], upload_dir)
    
    if not os.path.exists(upload_path):
        os.makedirs(upload_path)
    
    file.save(os.path.join(upload_path, file.filename))
    
    if request.form['format'] == 'csv' and file.filename.endswith('.csv'):
        df = pd.read_csv(os.path.join(upload_path, file.filename))
        
    elif request.form['format'] == 'xlsx' and file.filename.endswith('.xlsx'):
        df = pd.read_excel(os.path.join(upload_path, file.filename))
    
    return f"File '{file.filename}' has been saved successfully in {upload_dir} and processed!"

if __name__ == '__main__':
    app.run(debug=True)
