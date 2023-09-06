document.addEventListener('DOMContentLoaded', function () {
  const navLinks = document.querySelectorAll('.nav-links a');
  const navbar = document.querySelector('.navbar');
  const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
  const sections = document.querySelectorAll('section');

  // Smooth scroll navigation
  navLinks.forEach((link) => {
    link.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = link.getAttribute('href').substring(1);
      const targetSection = document.getElementById(targetId);
      if (targetSection) {
        window.scrollTo({
          top: targetSection.offsetTop - navbar.offsetHeight,
          behavior: 'smooth',
        });
      }
    });
  });

  // Highlight active navigation link
  window.addEventListener('scroll', () => {
    let currentSectionId = '';
    sections.forEach((section) => {
      const sectionTop = section.offsetTop - navbar.offsetHeight;
      const sectionBottom = sectionTop + section.clientHeight;
      if (window.scrollY >= sectionTop && window.scrollY < sectionBottom) {
        currentSectionId = section.getAttribute('id');
      }
    });
    navLinks.forEach((link) => {
      const linkId = link.getAttribute('href').substring(1);
      link.classList.toggle('active', linkId === currentSectionId);
    });
  });

  // Mobile navigation toggle
  mobileNavToggle.addEventListener('click', () => {
    navbar.classList.toggle('show-mobile-nav');
  });

  // Close mobile navigation on link click
  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      navbar.classList.remove('show-mobile-nav');
    });
  });

  // Scroll reveal animations
  ScrollReveal().reveal('.feature', {
    delay: 200,
    distance: '20px',
    origin: 'bottom',
  });

  ScrollReveal().reveal('.team-member', {
    delay: 200,
    distance: '20px',
    origin: 'bottom',
  });

  ScrollReveal().reveal('.cta-button', {
    delay: 400,
    distance: '20px',
    origin: 'bottom',
  });

  // Custom JavaScript code can be added here to further enhance your landing page.
});


 document.addEventListener('DOMContentLoaded', function () {
  // Get a reference to the "Go to App" button by its id
  const goToAppButton = document.getElementById('go-to-app-button');

  // Add a click event listener to the button
  goToAppButton.addEventListener('click', function (e) {
    e.preventDefault(); // Prevent the default link behavior

    // Navigate to the "compression.html" page
    window.location.href = '/compression.html';
  });
});
