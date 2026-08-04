use continuation_shared::{banner, section};

#[derive(Debug, Clone, Copy)]
struct State { temperature: f64, resilience: f64 }

#[derive(Debug, Clone, Copy)]
enum Repair { NoOp, Cool(f64), ReplaceCore }

fn score(s: State, r: Repair) -> f64 {
    let mut next = s;
    let (cost, risk) = match r {
        Repair::NoOp => (0.0, 0.0),
        Repair::Cool(x) => { next.temperature -= x; (x * 0.2, 0.1) }
        Repair::ReplaceCore => { next.temperature = 20.0; next.resilience -= 4.0; (5.0, 5.0) }
    };
    let deviation = (next.temperature - 20.0).abs();
    -(deviation + cost + risk) + next.resilience
}

fn main() {
    banner("Null Intervention",
        "Detection of deviation does not by itself warrant intervention.");

    let state = State { temperature: 21.0, resilience: 8.0 };
    let options = [Repair::NoOp, Repair::Cool(1.0), Repair::ReplaceCore];

    section("Scores");
    for option in options {
        println!("{option:?}: {:.2}", score(state, option));
    }

    section("Result");
    println!("When deviation is small and repair has costs, inaction can be rational.");
}
