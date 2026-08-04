use continuation_shared::{banner, section};

#[derive(Debug)]
struct State { x: f64, y: f64 }

fn scalar_model(s: &State) -> bool {
    (0.0..=10.0).contains(&s.x) && (0.0..=10.0).contains(&s.y)
}

fn relational_model(s: &State) -> bool {
    scalar_model(s) && (s.x - s.y).abs() <= 1.0
}

#[derive(Debug)]
enum RepairLevel { State, Constraint, Representation }

fn main() {
    banner("Representational Repair",
        "A model can fail while every variable it knows how to inspect appears valid.");

    let state = State { x: 2.0, y: 9.0 };
    section("Old representation");
    println!("scalar model reports admissible: {}", scalar_model(&state));

    section("Escalation");
    let level = RepairLevel::Representation;
    println!("repair level: {level:?}");
    println!("relational model reports admissible: {}", relational_model(&state));
    let _also_possible = (RepairLevel::State, RepairLevel::Constraint);

    section("Result");
    println!("The failure became visible only after the representation acquired relations.");
}
