import { localURL, createUser } from './api'; // Import the createUser function from api.js

function setCookie(name, value, days) {
    const expires = new Date();
    expires.setTime(expires.getTime() + days * 24 * 60 * 60 * 1000);
    document.cookie = `${name}=${value};expires=${expires.toUTCString()};path=/;SameSite=Lax`;
}

function getCookie(name) {
    const match = document.cookie.match(new RegExp(`(^| )${name}=([^;]+)`));
    return match ? match[2] : null;
}

function getOrCreateGuestID() {
    let guestID = getCookie("guestId");
    if (!guestID) {
        guestID = crypto.randomUUID(); // Generate a unique guest ID
        setCookie("guestId", guestID, 365); // Store for 1 year
        sendGuestIDToServer(guestID); // Store it in your database
    }
    return guestID;
}

function sendGuestIDToServer(guestID) {
    // Use the createUser function from api.js
    createUser(localURL, {
        is_guest: true,
        guest_id: guestID
    })
    .then(data => console.log('User created:', data))
    .catch(error => console.error('Error creating user:', error));
}

// Get or create the guest ID when the page loads
getOrCreateGuestID();