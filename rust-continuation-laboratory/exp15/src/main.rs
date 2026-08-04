use continuation_shared::{banner, section};

#[derive(Debug)]
enum Event { Push(&'static str), Refuse(usize) }

trait CollapseRule {
    fn project(&self, log: &[Event]) -> Vec<String>;
}

struct Active;
struct Refused;
struct FullHistory;

impl CollapseRule for Active {
    fn project(&self, log: &[Event]) -> Vec<String> {
        let refused: Vec<usize> = log.iter().filter_map(|e| if let Event::Refuse(i)=e {Some(*i)} else {None}).collect();
        log.iter().enumerate().filter_map(|(i,e)| match e {
            Event::Push(v) if !refused.contains(&i) => Some((*v).into()), _ => None
        }).collect()
    }
}
impl CollapseRule for Refused {
    fn project(&self, log: &[Event]) -> Vec<String> {
        log.iter().filter_map(|e| match e {
            Event::Refuse(i) => match log.get(*i) { Some(Event::Push(v)) => Some((*v).into()), _ => None },
            _ => None
        }).collect()
    }
}
impl CollapseRule for FullHistory {
    fn project(&self, log: &[Event]) -> Vec<String> {
        log.iter().map(|e| format!("{e:?}")).collect()
    }
}

fn main() {
    banner("Collapse as Projection",
        "One history supports several legitimate presents.");

    let log = vec![Event::Push("a"), Event::Push("b"), Event::Refuse(0)];
    section("Views");
    println!("active: {:?}", Active.project(&log));
    println!("refused: {:?}", Refused.project(&log));
    println!("history: {:?}", FullHistory.project(&log));
}
