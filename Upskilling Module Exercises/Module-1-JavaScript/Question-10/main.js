function showEvent(name = "Music Event") {

    console.log(name);
}

showEvent();

const event = {

    eventName: "Sports Meet",

    date: "15 June"
};

const {

    eventName,
    date

} = event;

console.log(eventName);

console.log(date);

const events = [

    "Music",

    "Sports"
];

const clonedEvents = [...events];

console.log(clonedEvents);