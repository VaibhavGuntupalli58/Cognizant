function addEvent(name) {

    console.log(`${name} Added`);
}

function registerUser(user) {

    console.log(`${user} Registered`);
}

function filterEventsByCategory(events,
                                callback) {

    return events.filter(callback);
}

const events = [

    {
        name: "Music Event",
        category: "Music"
    },

    {
        name: "Sports Event",
        category: "Sports"
    }
];

const musicEvents =
filterEventsByCategory(

    events,

    function(event) {

        return event.category === "Music";
    }
);

console.log(musicEvents);

function registrationCounter() {

    let count = 0;

    return function() {

        count++;

        return count;
    };
}

const counter = registrationCounter();

console.log(counter());

console.log(counter());
