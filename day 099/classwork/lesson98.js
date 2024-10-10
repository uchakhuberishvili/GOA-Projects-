class Vehicle {
    #speed;

    constructor(speed = 0) {
        this.#speed = speed;
    }

    accelerate(amount) {
        this.#speed += amount;
        return this.#speed;
    }

    getSpeed() {
        return this.#speed;
    }
}

class Bike extends Vehicle {
    constructor(speed) {
        super(speed);
    }

    increaseSpeed() {
        return this.accelerate(10);
    }
}


let myBike = new Bike(20);
console.log("Speed: " + myBike.getSpeed());
console.log("Accelerated Speed: " + myBike.increaseSpeed());


class Player {
    static playerCount = 0;

    constructor(name) {
        this.name = name;
        Player.playerCount++;
    }

    static getPlayerCount() {
        return Player.playerCount;
    }
}


let player1 = new Player("Alice");
let player2 = new Player("Bob");
console.log(Player.getPlayerCount());