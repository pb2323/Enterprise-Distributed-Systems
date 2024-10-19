import os
from flask import Flask, render_template, request, jsonify
import requests
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

# Configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Azure Computer Vision API settings
subscription_key = os.getenv('AZURE_SUBSCRIPTION_KEY')
endpoint = 'https://projectassignment.cognitiveservices.azure.com'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Call Azure OCR API
            extracted_text = azure_ocr(filepath)
            
            return jsonify({'text': extracted_text})
    
    return render_template('index.html')

def azure_ocr(image_path):
    ocr_url = f"{endpoint}/vision/v3.2/read/analyze"
    
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()
    
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream'
    }
    
    response = requests.post(ocr_url, headers=headers, data=image_data)
    response.raise_for_status()
    
    operation_url = response.headers["Operation-Location"]
    
    # Poll for result
    while True:
        result_response = requests.get(operation_url, headers={'Ocp-Apim-Subscription-Key': subscription_key})
        result = result_response.json()
        
        if result.get("status") == "succeeded":
            break
    
    extracted_text = ""
    for read_result in result.get("analyzeResult", {}).get("readResults", []):
        for line in read_result.get("lines", []):
            extracted_text += line.get("text", "") + "\n"
    
    return extracted_text

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)