// car object

let car = {
    make: 'bmw',
    model: '745li',
    year: 2010,
    getPrice: function() {
        // some calc
        return 5000;
    },
    printDescription: function() {
        console.log(this.make + ' ' + this.model);
    }
}

car.printDescription();
console.log(car.year);


// Don't do this.  Use . notation instead.
//console.log(car['year']);
//console.log(car[1]);

// add properties adhoc
var anotherCar = {};
anotherCar.whatever = 'bob';
console.log(anotherCar.whatever);

// Chaining through
var a = {
    myProperty: { b: 'hi' }
};
console.log(a.myProperty.b);