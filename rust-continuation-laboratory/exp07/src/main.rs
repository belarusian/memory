use continuation_shared::{banner, section, Admissible, Continue};

#[derive(Debug, Clone, Copy)]
struct State { energy: i32, integrity: i32 }

impl Admissible for State {
    fn is_admissible(&self) -> bool {
        self.energy >= 0 && self.integrity >= 0 && self.energy + self.integrity >= 4
    }
}

impl Continue for State {
    fn successors(&self) -> Vec<Self> {
        vec![
            State { energy: self.energy - 2, integrity: self.integrity + 1 },
            State { energy: self.energy + 1, integrity: self.integrity - 1 },
        ]
    }
}

fn depth(state: State, remaining: usize) -> usize {
    if !state.is_admissible() || remaining == 0 { return 0; }
    1 + state.successors().into_iter().map(|s| depth(s, remaining - 1)).max().unwrap_or(0)
}

fn main() {
    banner("Admissible State Space",
        "A locally attractive action may reduce the depth of viable continuation.");

    let start = State { energy: 4, integrity: 3 };
    section("Candidate successors");
    for s in start.successors() {
        println!("{s:?}, admissible={}, horizon={}", s.is_admissible(), depth(s, 8));
    }

    section("Result");
    println!("State quality depends partly on the future region it can still reach.");
}
