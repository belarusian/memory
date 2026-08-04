use continuation_shared::{banner, section};

#[derive(Debug, Clone, Copy)]
struct State { a: f64, b: f64, c: f64 }

fn scalar_valid(s: State) -> bool {
    [s.a, s.b, s.c].into_iter().all(|x| (0.0..=10.0).contains(&x))
}

fn structural_valid(s: State) -> bool {
    ((s.a + s.c) / 2.0 - s.b).abs() <= 0.5
}

fn coordinate_repair(mut s: State) -> State {
    s.b = s.b.clamp(0.0, 10.0);
    s
}

fn structural_repair(mut s: State) -> State {
    s.b = (s.a + s.c) / 2.0;
    s
}

fn main() {
    banner("Local Repair, Global Damage",
        "Scalar correction and structural restoration are different objectives.");

    let damaged = State { a: 2.0, b: 14.0, c: 8.0 };
    for (name, repaired) in [
        ("coordinate", coordinate_repair(damaged)),
        ("structural", structural_repair(damaged)),
    ] {
        section(name);
        println!("state: {repaired:?}");
        println!("scalar valid: {}", scalar_valid(repaired));
        println!("structural valid: {}", structural_valid(repaired));
    }
}
