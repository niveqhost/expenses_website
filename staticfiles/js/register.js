// @ts-nocheck
document.addEventListener("DOMContentLoaded", function () {
    const username_field = document.querySelector("#username-field");
    const feedback_area = document.querySelector(".invalid-feedback");

    username_field.addEventListener("keyup", function (event) {
        let username = event.target.value;
        username_field.classList.remove("is-invalid");
        feedback_area.style.display = "none";
        if (username.length > 0) {
            fetch("/account/validate-username", {
                body: JSON.stringify({ username: username }),
                method: "POST",
                headers: {
                    'Content-Type': 'application/json',
                },
            }).then(function (response) { return response.json(); })
            .then(function (data) {
                console.log(data.username_error);
            username_field.classList.add("is-invalid");
            feedback_area.style.display = "block";
            feedback_area.innerHTML = `<p>${data.username_error}</p>`;
            })
            .catch(function(error) { console.error("Error:", error) });
        }
    });
});