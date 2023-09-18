from flask import Flask, render_template, request, jsonify
from PIL import Image
import numpy as np
import os
import sys

app = Flask(__name__)

# Function to load an image from a path
def load_image(path):
    image = Image.open(path)
    return np.asarray(image) / 255

# Function to perform K-means clustering for image compression
def find_k_means(X, K, max_iters=10):
    # (Include your K-means code here)

# Function to compress and save an image
def compress_and_save_image(input_image_path, output_image_path, K=40, max_iters=20):
    try:
        assert os.path.isfile(input_image_path)
    except AssertionError:
        raise Exception('Image file not found.')

    # Load the image
    image = load_image(input_image_path)
    w, h, d = image.shape

    # Get the feature matrix X
    X = image.reshape((w * h, d))

    # Get colors using K-means clustering
    colors, _ = find_k_means(X, K, max_iters=max_iters)

    # Indexes for color for each pixel
    idx = find_closest_centroids(X, colors)

    # Reconstruct the image
    idx = np.array(idx, dtype=np.uint8)
    X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
    compressed_image = Image.fromarray(X_reconstructed)

    # Save reconstructed image to the specified path
    compressed_image.save(output_image_path)

