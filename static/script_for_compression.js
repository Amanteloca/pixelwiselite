document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('#upload-form');
  const compressButton = document.querySelector('#compress-button');
  const loadingIndicator = document.querySelector('#loading-indicator');
  const compressedImage = document.querySelector('#compressed-image');
  const compressedImageContainer = document.querySelector('#compressed-image-container');
  const errorMessage = document.querySelector('#error-message');

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    errorMessage.classList.add('hidden'); // Hide any previous error messages

    const formData = new FormData(form);
    
    try {
      compressButton.disabled = true;
      loadingIndicator.classList.remove('hidden');
      
      const response = await fetch('/compress', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        const compressedImageBlob = await response.blob();
        const compressedImageURL = URL.createObjectURL(compressedImageBlob);

        // Display the compressed image
        compressedImage.src = compressedImageURL;
        compressedImageContainer.classList.remove('hidden');
      } else {
        showError('Error while compressing the image');
      }
    } catch (error) {
      showError('An error occurred. Please try again later.');
    } finally {
      compressButton.disabled = false;
      loadingIndicator.classList.add('hidden');
    }
  });

  function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('hidden');
  }
});
