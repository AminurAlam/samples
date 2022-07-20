// comment
/*
multi line comment
write anything here
*/

#![allow(unused_variables)]


// This is a simple macro named `say_hello`.
macro_rules! say_hello {
    // `()` indicates that the macro takes no argument.
    () => {
        // The macro will expand into the contents of this block.
        println!("Hello!");
    };
}


fn main() {
    // printing something
    println!("Hello, world!");

    // data types
    let text: &str = "this is some text";  // string
    let number: i32 = 27;                  // signed integer
    let pi: f32 = 22.0/7.0;                // float
    let list = ("john doe", 36.2);         // array

    println!("value of pi is {} not {}", pi, number);
    println!("{:?} is an array", list);

    //// functions aka macro
    say_hello!();
}
