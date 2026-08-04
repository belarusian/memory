use continuation_shared::{banner, section};

#[derive(Debug, Clone)]
enum Distinction<A, B> {
    Left(A),
    Right(B),
    Unresolved { left: A, right: B },
}

#[derive(Debug)]
struct HistoricalDistinction<A, B> {
    current: Distinction<A, B>,
    history: Vec<&'static str>,
}

impl<A: Clone, B: Clone> HistoricalDistinction<A, B> {
    fn unresolved(left: A, right: B) -> Self {
        Self {
            current: Distinction::Unresolved { left, right },
            history: vec!["alternatives registered"],
        }
    }

    fn choose_left(&mut self) {
        let next = match &self.current {
            Distinction::Unresolved { left, .. } => Distinction::Left(left.clone()),
            Distinction::Left(left) => Distinction::Left(left.clone()),
            Distinction::Right(_) => panic!("cannot recover erased left alternative"),
        };
        self.current = next;
        self.history.push("left alternative selected");
    }

    fn choose_right(&mut self) {
        let next = match &self.current {
            Distinction::Unresolved { right, .. } => Distinction::Right(right.clone()),
            Distinction::Right(right) => Distinction::Right(right.clone()),
            Distinction::Left(_) => panic!("cannot recover erased right alternative"),
        };
        self.current = next;
        self.history.push("right alternative selected");
    }
}

fn visible_bit(d: &Distinction<&str, &str>) -> Option<bool> {
    match d {
        Distinction::Left(_) => Some(false),
        Distinction::Right(_) => Some(true),
        Distinction::Unresolved { .. } => None,
    }
}

fn main() {
    banner("Distinction Machine",
        "Equal present outputs can preserve different future possibilities.");

    let bare = false;
    let resolved = Distinction::Left("forest");
    let mut historical = HistoricalDistinction::unresolved("forest", "desert");
    historical.choose_left();

    let mut historical_other = HistoricalDistinction::unresolved("forest", "desert");
    historical_other.choose_right();

    section("Present outputs");
    println!("bare boolean: {bare}");
    println!("resolved distinction: {:?}", visible_bit(&resolved));
    println!("historical distinction (chose left): {:?}", visible_bit(&historical.current));
    println!("historical distinction (chose right): {:?}", visible_bit(&historical_other.current));

    section("Retained structure");
    println!("bare alternatives recoverable: no");
    println!("resolved alternatives recoverable: only by external convention");
    println!("historical events (left path): {:?}", historical.history);
    println!("historical events (right path): {:?}", historical_other.history);
    println!(
        "left-path and right-path outputs equal now: {}, but were reachable from the same unresolved origin only because that origin kept both alternatives live",
        visible_bit(&historical.current) == visible_bit(&resolved)
    );

    section("Result");
    println!("The three systems agree now, but do not support the same continuations.");
}
