use continuation_shared::{banner, section};

#[derive(Debug, Clone)]
struct Process { name: &'static str, next_fire: u64, interval: u64, runs: u64 }

fn run_earliest(processes: &mut [Process], steps: usize) {
    for _ in 0..steps {
        let i = processes.iter().enumerate()
            .min_by_key(|(_, p)| p.next_fire)
            .map(|(i, _)| i).unwrap();
        processes[i].runs += 1;
        processes[i].next_fire += processes[i].interval;
    }
}

fn main() {
    banner("Fair Continuation Scheduler",
        "Execution should follow the earliest unsatisfied continuation requirement.");

    let mut processes = [
        Process { name: "cardio", next_fire: 0, interval: 1, runs: 0 },
        Process { name: "immune", next_fire: 0, interval: 5, runs: 0 },
        Process { name: "repair", next_fire: 2, interval: 7, runs: 0 },
    ];

    run_earliest(&mut processes, 20);

    section("Runs");
    for p in &processes {
        println!("{}: {} runs, next obligation {}", p.name, p.runs, p.next_fire);
    }
}
