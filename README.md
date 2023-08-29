# PixelWiselite - Image Compression Algorithm 

PixelWiselite is a Python-based image compression algorithm that allows users to upload images, select compression quality, and receive compressed images as output. This project utilizes the Flask framework for web development and Pillow (PIL) for image processing. 

## Getting Started 

These instructions will guide you through setting up and running the PixelWiselite application locally. 

### Prerequisites 

- Python 3.x
- Flask
- Pillow 

### Installation 

1. Clone the repository: 

   ```bash
   git clone https://github.com/Amanteloca/pixelwiselite.git
   cd pixelwiselite 

2. Create a virtual environment (optional but recommended):python3 -m venv venv
source venv/bin/activate 

Install dependencies:pip install -r requirements.txt 

Usage 

1. Run the Flask app:python pixelwiselite.py 

2. Open a web browser and navigate to http://127.0.0.1:5000/ to access the web interface. 

3. Upload an image and select a compression quality. 

4. Click "Compress Image" to generate and download the compressed image. 

Folder Structure 

• pixelwiselite.py: The main Flask app script.
• pixelwiselite_image_compression.py: Module for image compression functions.
• static/: Folder to store static files (CSS, JavaScript).
• templates/: Folder to store HTML templates.
• uploads/: Folder to store uploaded images.
• compressed/: Folder to store compressed images. 

Features 

• User-friendly web interface for image compression.
• Custom image compression algorithm.
• Options to select compression quality.
• Downloadable compressed images. 

Contributing 

Contributions are welcome! To contribute, follow these steps:Fork the repository.Create a new branch for your feature or bug fix.Make your changes and submit a pull request. 

Authors 

Anthony Yeboah (@Amanteloca)

