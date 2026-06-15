function registerEvent() {

    alert("Registered Successfully");
}

function filterCategory(category) {

    console.log(
        "Selected Category:",
        category
    );
}

document
.getElementById("search")

.addEventListener(

    "keydown",

    function(event) {

        console.log(
            "Key Pressed:",
            event.key
        );
    }
);