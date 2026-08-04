use continuation_shared::{banner, section};

#[derive(Debug)]
struct Payload { name: String, children: Vec<String> }

fn take_ownership(value: Payload) -> Payload {
    println!("callee can reach: {} and {:?}", value.name, value.children);
    value
}

fn main() {
    banner("Reachability as Ownership",
        "A move transfers legal reachability while preserving the value.");

    let payload = Payload {
        name: "root".into(),
        children: vec!["alpha".into(), "beta".into()],
    };

    section("Before move");
    println!("caller reaches: {:?}", payload);

    let payload = take_ownership(payload);

    section("After return");
    println!("caller reaches again: {:?}", payload);
    println!("physical destruction during move: no");

    section("Result");
    println!("The trajectory changed authorities, not contents.");
}
