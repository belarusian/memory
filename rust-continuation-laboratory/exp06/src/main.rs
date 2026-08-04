use continuation_shared::{banner, section};

fn longest<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() >= b.len() { a } else { b }
}

fn main() {
    banner("Lifetime as Continuation Proof",
        "A reference carries a proof that its referent outlives the dependent computation.");

    let outer = String::from("persistent");
    section("Valid dependency");
    {
        let inner = String::from("brief");
        let chosen = longest(&outer, &inner);
        println!("chosen while both supports exist: {chosen}");
    }

    section("After inner continuation ends");
    println!("outer remains available: {outer}");
    println!("a reference to inner could not lawfully cross this boundary");

    section("Result");
    println!("The lifetime relation is a static proof about dependency through time.");
}
