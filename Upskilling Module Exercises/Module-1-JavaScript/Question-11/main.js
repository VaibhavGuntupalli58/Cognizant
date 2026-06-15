document
.getElementById("registerForm")

.addEventListener(

    "submit",

    function(event) {

        event.preventDefault();

        const form = event.target;

        const name =
        form.elements["username"].value;

        const email =
        form.elements["email"].value;

        if(name === "" || email === "") {

            document.getElementById("error")
            .innerHTML =
            "All fields are required";
        }

        else {

            document.getElementById("error")
            .innerHTML =
            "Form Submitted";
        }
    }
);