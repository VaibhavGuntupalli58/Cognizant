const container =
document.querySelector("#eventContainer");

const card =
document.createElement("div");

card.innerHTML =
"<h2>Music Event</h2>";

container.appendChild(card);

function register() {

    card.innerHTML =
    "<h2>Registered Successfully</h2>";
}

function cancelEvent() {

    card.innerHTML =
    "<h2>Registration Cancelled</h2>";
}