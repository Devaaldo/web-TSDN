from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"

        file = request.files['file']
        
        if file.filename == '':
            return "No selected file"

        if file:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            file_up_name = f"{timestamp}_{file.filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_up_name))
            return f"File uploaded successfully as {file_up_name}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)