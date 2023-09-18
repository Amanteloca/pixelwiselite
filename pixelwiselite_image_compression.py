import os
from PIL import Image
import numpy as np

def load_image(path):
    """ Load image from path. Return a numpy array """
    image = Image.open(path)
    return np.asarray(image) / 255

def initialize_K_centroids(X, K):
    """ Choose K points from X at random """
    m = len(X)
    return X[np.random.choice(m, K, replace=False), :]

def find_closest_centroids(X, centroids):
    m = len(X)
    c = np.zeros(m)

    for i in range(m):
        # Find distances
        distances = np.linalg.norm(X[i] - centroids, axis=1)

        # Assign closest cluster to c[i]
        c[i] = np.argmin(distances)

    return c

def compute_means(X, idx, K):
    _, n = X.shape
    centroids = np.zeros((K, n))
    for k in range(K):
        examples = X[np.where(idx == k)]
        mean = [np.mean(column) for column in examples.T]
        centroids[k] = mean
    return centroids

def find_k_means(X, K, max_iters=10):
    centroids = initialize_K_centroids(X, K)
    previous_centroids = centroids
    for _ in range(max_iters):
        idx = find_closest_centroids(X, centroids)
        centroids = compute_means(X, idx, K)
        if (previous_centroids==centroids).all():
            # The centroids aren't moving anymore.
            return centroids
        else:
            previous_centroids = centroids

    return centroids, idx

def compress_and_save_image(input_image, quality=40):
    try:
        # Load the image
        image = load_image(input_image)
        w, h, d = image.shape

        # Get the feature matrix X
        X = image.reshape((w * h, d))
        K = quality  # the number of colors in the image

        # Get colors
        colors, _ = find_k_means(X, K, max_iters=20)

        # Indexes for color for each pixel
        idx = find_closest_centroids(X, colors)

        # Reconstruct the image
        idx = np.array(idx, dtype=np.uint8)
        X_reconstructed = np.array(colors[idx, :] * 255, dtype=np.uint8).reshape((w, h, d))
        compressed_image = Image.fromarray(X_reconstructed)

        # Save reconstructed image to disk
        output_path = 'compressed_image.jpg'  # You can specify a different output path
        compressed_image.save(output_path)

        return output_path
    except Exception as e:
        return str(e)
