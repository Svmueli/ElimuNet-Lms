
// Function to show a confirmation dialog before deleting an item
function confirmDelete(itemType, itemName) {
    if (confirm(`Are you sure you want to delete this ${itemType}: ${itemName}?`)) {
        // If user confirms, proceed with deletion
        alert(`${itemType} "${itemName}" deleted successfully!`);
        // You can perform deletion logic here, such as making an AJAX request to delete the item from the server
    } else {
        // If user cancels, do nothing
        return false;
    }
}

// Function to toggle password visibility
function togglePasswordVisibility() {
    var passwordInput = document.getElementById('password');
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

// Example function for form validation
function validateForm() {
    var usernameInput = document.getElementById('username');
    var emailInput = document.getElementById('email');
    var passwordInput = document.getElementById('password');

    if (usernameInput.value === "") {
        alert("Please enter a username.");
        return false;
    }

    if (emailInput.value === "") {
        alert("Please enter an email address.");
        return false;
    }

    if (passwordInput.value === "") {
        alert("Please enter a password.");
        return false;
    }

    return true;
}
