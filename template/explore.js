// Get all the card elements
const cards = document.querySelectorAll('.flower-card');

// Add event listener to each card
cards.forEach(card => {
    card.addEventListener('click', () => {
        // Display details in the popup
        const title = card.getAttribute('data-title');
        const description = card.getAttribute('data-description');
        showPopup(title, description);
    });
});

function showPopup(title, description) {
    // Update popup content
    document.getElementById('popupTitle').innerText = title;
    document.getElementById('popupDescription').innerText = description;

    // Show the popup
    document.getElementById('popup').style.display = 'block';
}

function closePopup() {
    // Hide the popup
    document.getElementById('popup').style.display = 'none';
}