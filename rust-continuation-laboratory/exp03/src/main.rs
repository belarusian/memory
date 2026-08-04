use continuation_shared::{banner, section};
use std::collections::BTreeSet;

#[derive(Debug)]
struct World { values: [i32; 5] }

#[derive(Debug)]
struct Boundary { name: &'static str, observed: BTreeSet<usize> }

impl Boundary {
    fn observe(&self, world: &World) -> Vec<(usize, i32)> {
        self.observed.iter().map(|&i| (i, world.values[i])).collect()
    }
}

fn main() {
    banner("Boundary-Relative Object",
        "The same process yields different objects under different interfaces.");

    let mut world = World { values: [4, 8, 15, 16, 23] };
    let narrow = Boundary { name: "narrow", observed: [1, 2].into_iter().collect() };
    let wide = Boundary { name: "wide", observed: [0, 1, 2, 3].into_iter().collect() };

    section("Before perturbation");
    println!("{}: {:?}", narrow.name, narrow.observe(&world));
    println!("{}: {:?}", wide.name, wide.observe(&world));

    world.values[3] = 99;

    section("After change at node 3");
    println!("{}: {:?}", narrow.name, narrow.observe(&world));
    println!("{}: {:?}", wide.name, wide.observe(&world));

    section("Result");
    println!("The event exists in the world but not in every object induced from it.");
}
