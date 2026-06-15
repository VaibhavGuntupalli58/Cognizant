let events = [

    "Music Event",

    "Sports Event"
];

events.push("Baking Workshop");

console.log(events);

const musicEvents =
events.filter(function(event) {

    return event.includes("Music");
});

console.log(musicEvents);

const formatted =
events.map(function(event) {

    return `Workshop on ${event}`;
});

console.log(formatted);