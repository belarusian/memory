use continuation_shared::{banner, section};

#[derive(Debug, Clone, Copy)]
struct System { deviation: i32, budget: i32, failures_survived: i32 }

fn immediate(mut s: System, disturbances: &[i32]) -> System {
    for &d in disturbances {
        s.deviation += d;
        let cost = s.deviation.abs();
        s.budget -= cost;
        s.deviation = 0;
        if s.budget >= 0 { s.failures_survived += 1; } else { break; }
    }
    s
}

fn selective(mut s: System, disturbances: &[i32]) -> System {
    for &d in disturbances {
        s.deviation += d;
        if s.deviation.abs() >= 4 {
            let cost = s.deviation.abs();
            s.budget -= cost;
            s.deviation = 0;
        }
        if s.budget >= 0 { s.failures_survived += 1; } else { break; }
    }
    s
}

fn main() {
    banner("Repair Budget",
        "Correcting every deviation can exhaust capacity needed for later crises.");

    let start = System { deviation: 0, budget: 10, failures_survived: 0 };
    let disturbances = [1, 1, 1, 6, 2];

    section("Strategies");
    println!("immediate: {:?}", immediate(start, &disturbances));
    println!("selective: {:?}", selective(start, &disturbances));

    section("Result");
    println!("Tolerance can preserve resources for disturbances that threaten continuation.");
}
