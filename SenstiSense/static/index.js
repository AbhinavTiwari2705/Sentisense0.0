// set up event listeners for the navbar links
const navbarLinks = document.querySelectorAll('.nav-link');
navbarLinks.forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    // get the target element to scroll to
    const targetId = link.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    // scroll to the target element
    targetElement.scrollIntoView({ behavior: 'smooth' });
  });
});

// set up event listener for the login form submission
const loginForm = document.querySelector('#loginForm');
loginForm.addEventListener('submit', e => {
  e.preventDefault();
  // handle login form submission here
});

// set up event listener for the signup form submission
const signupForm = document.querySelector('#signupForm');
signupForm.addEventListener('submit', e => {
  e.preventDefault();
  // handle signup form submission here
});

// read in text file
const fileInput = document.querySelector('#fileInput');
fileInput.addEventListener('change', e => {
  const file = fileInput.files[0];
  const reader = new FileReader();
  reader.onload = event => {
    // do something with the file contents
    const contents = event.target.result;
  };
