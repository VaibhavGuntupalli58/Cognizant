fetch("https://jsonplaceholder.typicode.com/posts")

.then(function(response) {

    return response.json();
})

.then(function(data) {

    console.log(data);

    document.getElementById("loading")
    .innerHTML = "Data Loaded";
})

.catch(function(error) {

    console.log(error);
});

async function loadData() {

    try {

        const response =
        await fetch(
        "https://jsonplaceholder.typicode.com/posts"
        );

        const data =
        await response.json();

        console.log(data);
    }

    catch(error) {

        console.log(error);
    }
}

loadData();
