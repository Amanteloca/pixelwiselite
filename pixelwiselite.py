# Define the route to the landing page
@app.route('/')
def landing():
    return render_template('landing.html')

# Define the route for image compression page
@app.route('/compression')
def compression():
    return render_template('compression.html')

# Define the route to handle image compression
@app.route('/compress_image', methods=['POST'])
def compress_image():
    try:
        # Get the uploaded image and compression quality from the form
        uploaded_image = request.files['image']
        compression_quality = request.form['quality']

        # Set default input and output paths
        input_image_path = 'default_input_image.jpg'
        output_image_path = 'default_output_image.jpg'

        # Check if an image file was selected
        if uploaded_image.filename != '':
            # Compress and save the image using the specified paths
            compress_and_save_image(input_image_path, output_image_path)

            # Return the path to the compressed image
            return jsonify({'compressed_image_path': output_image_path})
        else:
            return jsonify({'error': 'No image selected'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
