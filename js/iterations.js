/*
for (i = 0; i < 10; i++) { // don't really need the let to declare i
    console.log(i);
}
*/

/*
// Iterate through an array
let a = [4, 8, 15, 16, 23, 42];
for (i = 0; i < a.length; i++) {
    console.log(a[i]);
}
*/

// Code snippet
/*
for (let index  = 0; index < array.length; index++) {
    const element = array[index];
    
}
*/

/* Example
let a = [4, 8, 15, 16, 23, 42];
for (let b = 0; b < a.length; b++) {
    const c = a[b];
    console.log(c);

}
*/

let x = 1;
while (x < 10) {
    console.log(x++);

    /*
    if (x == 7){
        break;
    }
    */
    if (x == 7) break; // short way.  Don't need brackets
}