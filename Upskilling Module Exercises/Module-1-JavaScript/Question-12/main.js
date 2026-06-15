function submitData() {

    setTimeout(function() {

        fetch(
        "https://jsonplaceholder.typicode.com/posts",

        {

            method: "POST",

            headers: {

                "Content-Type":
                "application/json"
            },

            body: JSON.stringify({

                name: "Bujji",

                event: "Music"
            })
        })

        .then(function(response) {

            return response.json();
        })

        .then(function(data) {

            document.getElementById("message")
            .innerHTML =
            "Registration Successful";

            console.log(data);
        })

        .catch(function(error) {

            document.getElementById("message")
            .innerHTML =
            "Registration Failed";

            console.log(error);
        });

    }, 2000);
}
