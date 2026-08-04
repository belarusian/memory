use continuation_shared::{banner, section};
use std::collections::BTreeMap;

#[derive(Debug)]
struct Node { admissible: bool, terminal: bool }

#[derive(Debug)]
struct System {
    nodes: Vec<Node>,
    edges: BTreeMap<usize, Vec<usize>>,
}

impl System {
    fn continuation_failures(&self) -> Vec<usize> {
        self.nodes.iter().enumerate().filter_map(|(i, node)| {
            if !node.admissible || node.terminal { return None; }
            let has_successor = self.edges.get(&i).into_iter().flatten()
                .any(|&j| self.nodes.get(j).map(|n| n.admissible).unwrap_or(false));
            (!has_successor).then_some(i)
        }).collect()
    }
}

fn main() {
    banner("Fundamental Continuation",
        "A state is viable only relative to an admissible reachable future.");

    let mut system = System {
        nodes: vec![
            Node { admissible: true, terminal: false },
            Node { admissible: true, terminal: false },
            Node { admissible: false, terminal: false },
            Node { admissible: true, terminal: true },
        ],
        edges: [(0, vec![1]), (1, vec![2])].into_iter().collect(),
    };

    section("Before repair");
    println!("continuation failures: {:?}", system.continuation_failures());

    system.edges.entry(1).or_default().push(3);

    section("After adding repair transition");
    println!("continuation failures: {:?}", system.continuation_failures());
}
