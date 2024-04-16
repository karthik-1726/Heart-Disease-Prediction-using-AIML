document.addEventListener('DOMContentLoaded', function() {
    const emailInput = document.getElementById('email');
    const passwordInput = document.getElementById('password');
    const messageContainer = document.getElementById('container1');

    // Add input event listeners to clear messages
    emailInput.addEventListener('input', clearMessages);
    passwordInput.addEventListener('input', clearMessages);

    function clearMessages() {
        messageContainer.innerHTML = ''; // Clear the messages
    }
});