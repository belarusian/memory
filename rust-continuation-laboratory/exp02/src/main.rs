use continuation_shared::{banner, section};

#[derive(Debug, Clone, PartialEq)]
struct State { temperature: f64, shape: i32 }

#[derive(Debug, Clone)]
struct Entity {
    id: u64,
    state: State,
    repairs: Vec<String>,
}

impl Entity {
    fn perturb(&mut self) {
        self.state.temperature += 18.0;
        self.state.shape += 1;
    }

    fn repair(&mut self) {
        let before = self.state.clone();
        self.state.temperature = 20.0;
        self.repairs.push(format!("cooled {:?} to {:?}", before, self.state));
    }
}

fn same_snapshot(a: &Entity, b: &Entity) -> bool { a.state == b.state }
fn same_identifier(a: &Entity, b: &Entity) -> bool { a.id == b.id }
fn same_continuation(a: &Entity, b: &Entity) -> bool {
    a.id == b.id && a.repairs.len() <= b.repairs.len()
}

fn main() {
    banner("Identity Through Repair",
        "A repaired entity may differ materially while remaining the same continuation.");

    let original = Entity { id: 7, state: State { temperature: 20.0, shape: 4 }, repairs: vec![] };
    let mut later = original.clone();
    later.perturb();
    later.repair();

    section("Comparisons");
    println!("same snapshot: {}", same_snapshot(&original, &later));
    println!("same identifier: {}", same_identifier(&original, &later));
    println!("same continuation: {}", same_continuation(&original, &later));
    println!("repair history: {:?}", later.repairs);

    section("Result");
    println!("Static equality was lost; historical continuity was not.");
}
