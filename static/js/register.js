// @ts-nocheck
document.addEventListener("DOMContentLoaded", function () {
    // User Name
    const username_field = document.querySelector("#username-field");
    const username_valid_feedback = document.querySelector(".username-valid-feedback");
    const username_invalid_feedback = document.querySelector(".username-invalid-feedback");
    // Email
    const email_field = document.querySelector("#email-field");
    const email_valid_feedback = document.querySelector(".email-valid-feedback");
    const email_invalid_feedback = document.querySelector(".email-invalid-feedback");

    username_field.addEventListener("keyup", function (event) {
        let username = event.target.value;
        username_field.classList.remove("is-invalid");
        username_field.classList.remove("is-valid");
        username_invalid_feedback.style.display = "none";
        username_valid_feedback.style.display = "none";
        if (username.length > 0) {
            fetch("/account/validate-username", {
                body: JSON.stringify({ username: username }),
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
            }).then(function (response) { return response.json(); })
            .then(function (data) {
                if (data.username_error != undefined) {
                    username_field.classList.add("is-invalid");
                    username_invalid_feedback.style.display = "block";
                    username_invalid_feedback.innerHTML = `<p>${data.username_error}</p>`;
                } else {
                    username_field.classList.add("is-valid");
                    username_valid_feedback.style.display = "block";
                    username_valid_feedback.textContent = "Look goods.";
                }
            })
            .catch(function(error) { console.error("Username Error:", error) });
        }
    });

    email_field.addEventListener("keyup", function (event) {
        let email = event.target.value;
        email_field.classList.remove("is-invalid");
        email_field.classList.remove("is-valid");
        email_valid_feedback.style.display = "none";
        email_invalid_feedback.style.display = "none";
        if (email.length > 0) {
            fetch("/account/validate-email", {
                body: JSON.stringify({ email: email }),
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
            }).then(function (response) { return response.json(); })
            .then(function (data) {
                if (data.email_error != undefined) {
                    email_field.classList.add("is-invalid");
                    email_invalid_feedback.style.display = "block";
                    email_invalid_feedback.innerHTML = `<p>${data.email_error}</p>`;
                } else {
                    email_field.classList.add("is-valid");
                    email_valid_feedback.style.display = "block";
                    email_valid_feedback.textContent = "Look goods.";
                }
            })
            .catch(function(error) { console.error("Email error:", error) });
        }
    });
});
