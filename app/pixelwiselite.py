from flask import Flask, render_template, request, jsonify, send_from_directory
import os
from pixelwiselite_image_compression import compress_and_save_image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'  # Replace with your desired upload folder
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Default route for the web interface
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to handle image compression via POST request
@app.route('/api/compress', methods=['POST'])
def api_compress():
    try:
        if 'image' not in request.files:
            return jsonify({'error': 'No image part'}), 400

        file = request.files['image']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if file and allowed_file(file.filename):
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)

            compressed_filename = compress_and_save_image(filename, app.config['UPLOAD_FOLDER'], 800, compression_quality=70)
            if compressed_filename:
                return send_from_directory(app.config['UPLOAD_FOLDER'], compressed_filename, as_attachment=True)
            else:
                return jsonify({'error': 'Error occurred during compression'}), 500
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)
