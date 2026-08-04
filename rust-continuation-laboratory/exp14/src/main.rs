use continuation_shared::{banner, section};

#[derive(Debug)]
enum Event { Push(i32), Refuse(usize) }

fn stack(log: &[Event]) -> Vec<i32> {
    let refused: Vec<usize> = log.iter().filter_map(|e| match e {
        Event::Refuse(i) => Some(*i), _ => None
    }).collect();

    log.iter().enumerate().filter_map(|(i, e)| match e {
        Event::Push(v) if !refused.contains(&i) => Some(*v),
        _ => None
    }).collect()
}

fn pop(log: &mut Vec<Event>) -> Option<i32> {
    let current = stack(log);
    let value = *current.last()?;
    let id = log.iter().enumerate().rev().find_map(|(i, e)| match e {
        Event::Push(v) if *v == value => Some(i),
        _ => None
    })?;
    log.push(Event::Refuse(id));
    Some(value)
}

fn main() {
    banner("Refusal Without Erasure",
        "Logical removal can preserve the distinction in an append-only account.");

    let mut log = vec![Event::Push(10), Event::Push(20), Event::Push(30)];
    section("Before pop");
    println!("stack: {:?}", stack(&log));
    println!("popped: {:?}", pop(&mut log));

    section("After pop");
    println!("stack: {:?}", stack(&log));
    println!("history: {log:?}");
}
