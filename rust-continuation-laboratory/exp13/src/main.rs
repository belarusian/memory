use continuation_shared::{banner, section};

#[derive(Debug)]
enum Event<T> { Assert(T), Refuse(usize) }

fn visible<T: Clone>(events: &[Event<T>]) -> Vec<T> {
    let refused: Vec<usize> = events.iter().filter_map(|e| {
        if let Event::Refuse(id) = e { Some(*id) } else { None }
    }).collect();

    events.iter().enumerate().filter_map(|(id, e)| match e {
        Event::Assert(value) if !refused.contains(&id) => Some(value.clone()),
        _ => None,
    }).collect()
}

fn main() {
    banner("Monotonic Ledger",
        "History grows while the projected present changes.");

    let mut ledger = vec![Event::Assert("alpha"), Event::Assert("beta")];
    section("Initial");
    println!("ledger: {ledger:?}");
    println!("visible: {:?}", visible(&ledger));

    ledger.push(Event::Refuse(0));
    section("After refusal");
    println!("ledger: {ledger:?}");
    println!("visible: {:?}", visible(&ledger));

    section("Result");
    println!("Alpha disappeared from the view but remained in history.");
}
