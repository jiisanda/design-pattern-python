/*
Singleton Pattern is perceived as unsafe, because to avoid all sorts of concurrency issue, 
the function block that is either reading or writing to a mutable static variable
should be marked as unsafe block.

*/
use std::sync::Mutex;

static ARRAY: Mutex<Vec<i32>> = Mutex::new(Vec::new());

fn do_a_call() {
    ARRAY.lock().unwrap().push(1);
}

fn main() {
    do_a_call();
    do_a_call();
    do_a_call();

    println!("Called {} times", ARRAY.lock().unwrap().len());
}
