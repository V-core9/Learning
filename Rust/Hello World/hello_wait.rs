use std::{thread, time};

fn wait_for(timeout:u64)-> () {

    let ten_millis = time::Duration::from_millis(timeout);
    let now = time::Instant::now();

    thread::sleep(ten_millis);

    assert!(now.elapsed() >= ten_millis);
}

// This is the main function
fn main() {
    // Statements here are executed when the compiled binary is called

    // Print text to the console
    println!("Hello World!");

    wait_for(10000);
}
