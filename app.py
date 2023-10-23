# app.py
from flask import Flask, request, render_template
import boto3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    s3 = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')
    s3.upload_fileobj(file, '', file.filename)
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
