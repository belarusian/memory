use continuation_shared::{banner, section};
use std::collections::BTreeMap;

#[derive(Debug, Clone, Copy)]
enum Terrain { Plain, Ridge }

#[derive(Default)]
struct World { cells: BTreeMap<(i32, i32), Terrain> }

impl World {
    fn resolve(&mut self, x: i32, y: i32) -> Terrain {
        if let Some(&cell) = self.cells.get(&(x, y)) { return cell; }
        let neighbor_ridge = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            .iter().filter_map(|p| self.cells.get(p))
            .any(|t| matches!(t, Terrain::Ridge));
        let terrain = if neighbor_ridge || (x * 31 + y * 17).rem_euclid(5) == 0 {
            Terrain::Ridge
        } else {
            Terrain::Plain
        };
        self.cells.insert((x, y), terrain);
        terrain
    }
}

fn main() {
    banner("Persistent Generative World",
        "Generation becomes world-building when outcomes persist and constrain neighbors.");

    let mut world = World::default();
    section("First traversal");
    for x in 0..6 { println!("({x},0) -> {:?}", world.resolve(x, 0)); }

    section("Return traversal");
    for x in (0..6).rev() { println!("({x},0) -> {:?}", world.resolve(x, 0)); }

    section("Result");
    println!("resolved cells stored: {}", world.cells.len());
}
