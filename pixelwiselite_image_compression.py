from PIL import Image, ImageFilter
import os
import logging

def compress_and_save_image(input_path, output_folder, max_width, compression_quality=85):
    try:
        # Open the image
        with Image.open(input_path) as image:
            # Apply image enhancements (e.g., sharpening)
            enhanced_image = apply_image_enhancements(image)

            # Calculate the new height to maintain aspect ratio
            width, height = enhanced_image.size
            new_height = int(max_width * height / width)

            # Resize the image using Lanczos resampling for better quality
            resized_image = enhanced_image.resize((max_width, new_height), Image.LANCZOS)

            # Create the output path for the compressed image
            compressed_filename = f"compressed_{os.path.basename(input_path)}"
            compressed_path = os.path.join(output_folder, compressed_filename)

            # Save the compressed image in WebP format for efficient compression
            resized_image.save(compressed_path, "WebP", quality=compression_quality)

            return compressed_path  # Return the path of the compressed image
    except FileNotFoundError:
        logging.error("Input image file not found.")
    except Exception as e:
        logging.error(f"Error during compression: {e}")
    return None

def apply_image_enhancements(image):
    # Apply advanced image enhancements (e.g., sharpening) using PIL's filters
    enhanced_image = image.filter(ImageFilter.SHARPEN)
    return enhanced_image
