function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

// Function to validate the phone number format
function validatePhone(phone) {
    const regex = /^\d{10}$/;
    return regex.test(phone);
}

// Function to handle form submission
function handleSubmit(event) {
    // Validate inputs
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;

    if (name.trim() === '') {
        alert('Please enter your name.');
        return;
    }

    if (email.trim() === '' || !validateEmail(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    if (phone.trim() === '' || !validatePhone(phone)) {
        alert('Please enter a valid 10-digit phone number.');
        return;
    }

    if (message.trim() === '') {
        alert('Please enter your message.');
        return;
    }

    // If all inputs are valid, the form will submit normally
}

// Attach event listener to the form submit event
document.getElementById('feedback-form').addEventListener('submit', handleSubmit);