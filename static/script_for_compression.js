document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('#upload-form');
  const compressedImage = document.querySelector('#compressed-image');
  const compressedImageContainer = document.querySelector('#compressed-image-container');
  const uploadButton = document.querySelector('#upload-button');
  const loadingIndicator = document.querySelector('#loading-indicator');
  const errorMessage = document.querySelector('#error-message');

  form.addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData(form);

    // Disable the upload button while processing
    uploadButton.disabled = true;
    loadingIndicator.style.display = 'block';

    try {
      const response = await fetch('/compression', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const compressedImageBlob = await response.blob();
        const compressedImageURL = URL.createObjectURL(compressedImageBlob);

        // Display the compressed image
        compressedImage.src = compressedImageURL;
        compressedImageContainer.style.display = 'block'; // Show the image container
        errorMessage.style.display = 'none'; // Hide error message if previously shown
      } else {
        errorMessage.textContent = 'Error while compressing the image';
        errorMessage.style.display = 'block'; // Show error message
      }
    } catch (error) {
      errorMessage.textContent = 'An unexpected error occurred';
      errorMessage.style.display = 'block'; // Show error message
    } finally {
      // Re-enable the upload button and hide loading indicator
      uploadButton.disabled = false;
      loadingIndicator.style.display = 'none';
    }
  });
});
