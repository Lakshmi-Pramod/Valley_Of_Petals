const sign_in_btn=document.querySelector("#sign_in_btn");
const sign_up_btn=document.querySelector("#sign_up_btn");
const container=document.querySelector(".c");
const sign_in_btn2=document.querySelector("#sign_in_btn2");
const sign_up_btn2=document.querySelector("#sign_up_btn2");

sign_up_btn.addEventListener("click",() =>{
    container.classList.add("sign_up_mode");
});

sign_in_btn.addEventListener("click",() =>{
    container.classList.remove("sign_up_mode");
});

sign_up_btn2.addEventListener("click",() =>{
    container.classList.add("sign_up_mode2");
}); 

sign_in_btn2.addEventListener("click",() =>{
    container.classList.remove("sign_up_mode2");
});


document.getElementById('loginAsAdminBtn').addEventListener('click', function () {
    // Redirect to the admin login page or any other page you want
    window.location.href = 'http://localhost:8000/admin';
});


function validcheck() {
    var isNotEmptyUsername = document.getElementById("Username").value !== '';
    var isNotEmptyEmail = document.getElementById("email").value !== '';
    var isValidEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(document.getElementById("email").value);
    var isNotEmptyPassword = document.getElementById("pass1").value !== '';
    var isPasswordEqual = document.getElementById("pass1").value === document.getElementById("pass2").value;

    var errorMessage = document.getElementById("error-message-signup");

    errorMessage.innerHTML = ""; // Clear any previous error messages

    if (!isNotEmptyUsername) {
        errorMessage.innerHTML += "Username is empty.<br>";
    }

    if (!isNotEmptyEmail) {
        errorMessage.innerHTML += "Email is empty.<br>";
    } else if (!isValidEmail) {
        errorMessage.innerHTML += "Email is invalid.<br>";
    }

    if (!isNotEmptyPassword) {
        errorMessage.innerHTML += "Password is empty.<br>";
    } else if (!isPasswordEqual) {
        errorMessage.innerHTML += "Passwords do not match.<br>";
    }

    // Check if there are any error messages
    if (errorMessage.innerHTML !== "") {
        return false; // Prevent form submission
    } else {
        // If no errors, allow form submission
        window.alert("Sign up Successful!!");
        return true;
    }
}


const popup=document.getElementById('popup');
function validcheck1() {
    var isValidEmail = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(document.getElementById("email").value);
    var isNotEmptyEmail = document.getElementById("email").value !== '';
    var isNotEmptyPassword = document.getElementById("pass0").value !== '';
    var isValidPassword = /^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z]).{8,}$/.test(document.getElementById("pass0").value);

    var errorMessage = document.getElementById("error-message");

    if (!isNotEmptyEmail && !isNotEmptyPassword) {
        errorMessage.innerHTML = "Email and password are empty";
        return false; // Prevent form submission
    } else if (!isNotEmptyEmail) {
        errorMessage.innerHTML = "Email is empty";
        return false; // Prevent form submission
    } else if (!isValidEmail) {
        errorMessage.innerHTML = "Email is invalid";
        return false; // Prevent form submission
    } else if (!isNotEmptyPassword) {
        errorMessage.innerHTML = "Password is empty";
        return false; // Prevent form submission
    } else if (!isValidPassword) {
        errorMessage.innerHTML = "Password does not meet the criteria";
        return false; // Prevent form submission
    } else {
        errorMessage.innerHTML = ""; // Clear any previous error messages
        window.alert("Login Successful!!");
        return true; // Allow form submission
    }
}



function closeslide()
  {
    popup.classList.remove('open-slide')
  }