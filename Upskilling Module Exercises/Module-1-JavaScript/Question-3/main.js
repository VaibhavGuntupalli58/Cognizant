const events = [

    {
        name: "Music Show",
        seats: 20,
        status: "upcoming"
    },

    {
        name: "Old Event",
        seats: 0,
        status: "past"
    }
];

events.forEach(function(event) {

    if(event.status === "upcoming"
       && event.seats > 0) {

        console.log(event.name);
    }

    else {

        console.log(
            `${event.name} is unavailable`
        );
    }
});

try {

    let seats = 0;

    if(seats <= 0) {

        throw "No Seats Available";
    }

    console.log("Registration Successful");
}

catch(error) {

    console.log("Error:", error);
}
