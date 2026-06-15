function submitForm() {

    console.log("Form Submission Started");

    let username = "Bujji";

    debugger;

    console.log("Username:", username);

    console.log("Fetch Request Sent");

    fetch(
    "https://jsonplaceholder.typicode.com/posts"
    )

    .then(function(response) {

        return response.json();
    })

    .then(function(data) {

        console.log(data);
    });
}
