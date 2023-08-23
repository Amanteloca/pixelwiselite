from PIL import Image
import os
import logging

def compress_and_save_image(input_path, output_folder, max_width, compression_quality=85):
    try:
        # Open the image
        with Image.open(input_path) as image:
            # Calculate the new height to maintain aspect ratio
            width, height = image.size
            new_height = int(max_width * height / width)
            
            # Resize the image
            resized_image = image.resize((max_width, new_height), Image.ANTIALIAS)
            
            # Create the output path for the compressed image
            compressed_filename = f"compressed_{os.path.basename(input_path)}"
            compressed_path = os.path.join(output_folder, compressed_filename)
            
            # Save the compressed image with specified quality
            resized_image.save(compressed_path, quality=compression_quality)
            
            return compressed_filename  # Return the filename of the compressed image
    except FileNotFoundError:
        logging.error("Input image file not found.")
    except Exception as e:
        logging.error(f"Error during compression: {e}")
    return None
