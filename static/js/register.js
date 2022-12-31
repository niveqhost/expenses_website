// @ts-nocheck
document.addEventListener("DOMContentLoaded", function () {
    // User Name
    const username_field = document.querySelector("#username-field");
    const username_valid_feedback = document.querySelector(".valid-feedback");
    const username_invalid_feedback = document.querySelector(".invalid-feedback");
    // Email
    const email_field = document.querySelector("#email-field");
    const email_valid_feedback = document.querySelector(".email-valid-feedback");
    const email_invalid_feedback = document.querySelector(".email-invalid-feedback");

    username_field.addEventListener("keyup", function(event) {
        const username = event.target.value;
    
        username_field.classList.remove("is-valid");
        username_field.classList.remove("is-invalid");
        username_valid_feedback.style.display = "none";
        username_invalid_feedback.style.display = "none";

        if (username.length > 0) {
            fetch("/account/validate-username", {
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username: username }),
                method: "POST",
            }).then(function (response) { return response.json(); })
            .then(function(data) {
                if (data.username_error) {
                    username_field.classList.remove("is-valid");
                    username_field.classList.add("is-invalid");
                    username_valid_feedback.style.display = "none";
                    username_invalid_feedback.style.display = "block";
                    username_invalid_feedback.textContent = `${data.username_error}`;
                } else {
                    username_field.classList.remove("is-invalid");
                    username_field.classList.add("is-valid");
                    username_invalid_feedback.style.display = "none";
                    username_valid_feedback.style.display = "block";
                    username_valid_feedback.textContent = "Looks good.";
                }
            }).catch(function (error) { throw error; });
        }
    });

    email_field.addEventListener("keyup", function(event) {
        const email = event.target.value;

        email_field.classList.remove("is-valid");
        email_field.classList.remove("is-invalid");
        email_valid_feedback.style.display = "none";
        email_invalid_feedback.style.display = "none";

        if (email.length > 0) {
            fetch("/account/validate-email", {
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ email: email }),
                method: "POST",
            }).then(function (response) { return response.json(); })
            .then(function (data) {
                if (data.email_error) {
                    email_field.classList.remove("is-valid");
                    email_field.classList.add("is-invalid");
                    email_valid_feedback.style.display = "none";
                    email_invalid_feedback.style.display = "block";
                    email_invalid_feedback.textContent = `${data.email_error}`;
                } else {
                    email_field.classList.remove("is-invalid");
                    email_field.classList.add("is-valid");
                    email_invalid_feedback.style.display = "none";
                    email_valid_feedback.style.display = "block";
                    email_valid_feedback.textContent = "Looks good.";
                }
            }).catch(function (error) { throw error; });
        }
    });
});