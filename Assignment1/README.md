# OCR Analytics Web Application

This project is a web-based OCR (Optical Character Recognition) system that allows users to upload images and extract text using Azure's Computer Vision API.

Project documentation report - (https://docs.google.com/document/d/12bFINw4jjF1u3INOXG_-5HugeatJ4NRHl9PXrZELy40/edit?usp=sharing)[https://docs.google.com/document/d/12bFINw4jjF1u3INOXG_-5HugeatJ4NRHl9PXrZELy40/edit?usp=sharing]

## Features

- Image upload functionality
- Text extraction using Azure Computer Vision API
- Real-time display of extracted text
- Simple and intuitive user interface

## Technologies Used

- Backend: Flask (Python)
- Frontend: HTML, JavaScript
- OCR: Azure Computer Vision API

## Prerequisites

- Python 3.7+
- Flask
- Requests library
- Azure subscription with Computer Vision API access

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/ocr-analytics-app.git
   cd ocr-analytics-app
   ```

2. Install the required Python packages:
   ```
   pip3 install -r requirements.txt
   ```

3. Set up your Azure Computer Vision API credentials:
   - Open `app.py`
   - Replace `subscription_key` and `endpoint` with your Azure API credentials

4. Run the Flask application:
   ```
   python app.py
   ```

5. Open a web browser and navigate to `http://127.0.0.1:5000`

## Usage

1. On the web interface, click "Choose File" to select an image from your computer.
2. Click "Analyze Image" to upload the image and extract text.
3. The extracted text will be displayed on the page once processing is complete.

## Project Structure

- `app.py`: Main Flask application file
- `templates/index.html`: HTML template for the web interface
- `uploads/`: Directory for temporarily storing uploaded images
