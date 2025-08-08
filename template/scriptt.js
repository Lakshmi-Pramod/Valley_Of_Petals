// Your existing JavaScript code
var lastScrollTop;
navbar = document.querySelector('.navbar');
window.addEventListener('scroll', function(){
    var scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    if (scrollTop > lastScrollTop) {
        navbar.style.top = '-80px';
    } else {
        navbar.style.top = '0';
    }
    lastScrollTop = scrollTop;
});

const popup = document.getElementById('popup');
const closeButton = document.getElementById('close-button');
const popupImage = document.getElementById('popup-image');
const popupTitle = document.getElementById('popup-title');
const popupDescription = document.getElementById('popup-description');

// Flora cards
const floraCards = document.querySelectorAll('.flora-card');
floraCards.forEach((card) => {
    card.addEventListener('click', (event) => {
        const imgSrc = card.querySelector('img').src;
        const title = card.querySelector('h2').textContent;
        const description = card.querySelector('p').textContent;

        // Populate popup content
        popupImage.src = imgSrc;
        popupImage.alt = title;
        popupTitle.textContent = title;
        popupDescription.textContent = description;

        // Display the popup
        popup.style.display = 'block';
    });
});

// Close the popup when clicking the close button
closeButton.addEventListener('click', closePopup);

// Close the popup when clicking outside
window.addEventListener('click', (event) => {
    if (event.target === popup) {
        closePopup();
    }
});

// Prevent clicks inside the popup from closing it
popup.addEventListener('click', (event) => {
    event.stopPropagation();
});

function closePopup() {
    popup.style.display = 'none';
}
