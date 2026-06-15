function Event(name, seats) {

    this.name = name;

    this.seats = seats;
}

Event.prototype.checkAvailability =
function() {

    if(this.seats > 0) {

        console.log("Seats Available");
    }

    else {

        console.log("No Seats Available");
    }
};

const event1 =
new Event("Music Show", 25);

event1.checkAvailability();

console.log(
    Object.entries(event1)
);
