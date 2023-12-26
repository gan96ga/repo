from flask import Flask, render_template, send_file
from google.cloud import storage
import os

app = Flask(__name__)

# Replace 'your-bucket-name' with your GCP Storage bucket name
BUCKET_NAME = 'bkt-26dec-ganga-v2'
'

# Configure this with your GCP credentials JSON file
# Ensure that the environment variable GOOGLE_APPLICATION_CREDENTIALS points to the file path
# Example: export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
storage_client = storage.Client()

@app.route('/')
def index():
    return render_template('index.html', message='Hello, GCP!')

@app.route('/upload')
def upload_file():
    # Replace 'your-file.txt' with the file you want to upload
    file_name = 'rep.txt'
    blob = storage_client.bucket(BUCKET_NAME).blob(file_name)
    
    # Replace '/path/to/your/local/file.txt' with the local path of the file you want to upload
    blob.upload_from_filename('D:\OneDrive - Tata Power\Desktop\test\rep.txt')
    
    return f'File {file_name} uploaded to {BUCKET_NAME}'

@app.route('/download/<filename>')
def download_file(filename):
    # Replace 'your-download-folder' with the folder where you want to save the downloaded files
    download_folder = 'test'
    
    # Ensure the folder exists, create it if necessary
    os.makedirs(download_folder, exist_ok=True)
    
    # Download the file from GCP Storage
    blob = storage_client.bucket(BUCKET_NAME).blob(filename)
    blob.download_to_filename(os.path.join(download_folder, filename))
    
    return send_file(os.path.join(download_folder, filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
