use continuation_shared::{banner, bool_word, section};
use std::cell::RefCell;
use std::rc::Rc;

/// A budget shared by reference, not by message. Two systems that never
/// call each other, and hold no field naming the other, can still make each
/// other's moves inadmissible by drawing down the same account.
struct Budget {
    remaining: RefCell<f64>,
}

impl Budget {
    fn new(amount: f64) -> Rc<Self> {
        Rc::new(Self { remaining: RefCell::new(amount) })
    }

    fn try_spend(&self, cost: f64) -> bool {
        let mut r = self.remaining.borrow_mut();
        if *r >= cost {
            *r -= cost;
            true
        } else {
            false
        }
    }

    fn balance(&self) -> f64 {
        *self.remaining.borrow()
    }
}

struct Subsystem {
    name: &'static str,
    budget: Rc<Budget>,
    moves_made: u32,
}

impl Subsystem {
    fn attempt_move(&mut self, local_cost: f64) -> bool {
        let ok = self.budget.try_spend(local_cost);
        if ok {
            self.moves_made += 1;
        }
        ok
    }
}

fn main() {
    banner(
        "Shared Admissibility Budget",
        "A move can be locally cheap and globally inadmissible, without any direct coupling between the systems that made it so.",
    );

    let shared = Budget::new(10.0);
    let mut system_a = Subsystem { name: "A", budget: Rc::clone(&shared), moves_made: 0 };
    let mut system_b = Subsystem { name: "B", budget: Rc::clone(&shared), moves_made: 0 };

    section("Independent local histories");
    println!("system A knows nothing about system B's state or existence");
    println!("system B knows nothing about system A's state or existence");
    println!("both hold only a reference to the same account");

    section("System B spends first");
    for cost in [4.0, 3.0, 2.0] {
        let ok = system_b.attempt_move(cost);
        println!(
            "system {} attempts move costing {cost}: {} (balance now {})",
            system_b.name, bool_word(ok), shared.balance()
        );
    }

    section("System A attempts a locally cheap move");
    let a_cost = 2.0;
    let a_ok = system_a.attempt_move(a_cost);
    println!(
        "system {} attempts move costing {a_cost}, which A alone would always consider admissible: {}",
        system_a.name, bool_word(a_ok)
    );
    println!("balance after A's attempt: {}", shared.balance());

    section("Result");
    println!(
        "{}'s moves made: {}, {}'s moves made: {}",
        system_a.name, system_a.moves_made, system_b.name, system_b.moves_made
    );
    println!(
        "A's move was refused for a reason invisible to A's own local state: {}",
        bool_word(!a_ok)
    );
    println!("The constraint that decided admissibility was never local to either subsystem; it lived in the shared account, not in any message between them.");
}
