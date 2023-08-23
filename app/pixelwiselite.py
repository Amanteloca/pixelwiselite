from flask import Flask, render_template, request, send_from_directory
import os
from pixelwiselite_image_compression import compress_and_save_image  # Import the image compression function
import logging

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Replace with your desired upload folder
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    try:
        if 'image' not in request.files:
            return 'No image part'

        file = request.files['image']

        if file.filename == '':
            return 'No selected file'

        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            compressed_filename = compress_and_save_image(filename, app.config['UPLOAD_FOLDER'], 800, compression_quality=70)
            if compressed_filename:
                return send_from_directory(app.config['UPLOAD_FOLDER'], compressed_filename, as_attachment=True)
            else:
                return 'Error occurred during compression'
    except Exception as e:
        logging.error(f"Error during compression: {e}")
        return 'An error occurred'

if __name__ == '__main__':
    app.run(debug=True)
