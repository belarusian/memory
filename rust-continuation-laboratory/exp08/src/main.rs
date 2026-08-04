use continuation_shared::{banner, section, Admissible};

#[derive(Debug)]
struct Reservoir { pressure: f64 }
impl Admissible for Reservoir {
    fn is_admissible(&self) -> bool { (0.0..=10.0).contains(&self.pressure) }
}

#[derive(Debug)]
struct Coupled { left: Reservoir, right: Reservoir }
impl Admissible for Coupled {
    fn is_admissible(&self) -> bool {
        self.left.is_admissible()
            && self.right.is_admissible()
            && (self.left.pressure - self.right.pressure).abs() <= 3.0
    }
}

fn main() {
    banner("Hierarchical Admissibility",
        "Components can each satisfy their bounds while their relation fails.");

    let system = Coupled {
        left: Reservoir { pressure: 9.0 },
        right: Reservoir { pressure: 2.0 },
    };

    section("Checks");
    println!("left admissible: {}", system.left.is_admissible());
    println!("right admissible: {}", system.right.is_admissible());
    println!("coupled system admissible: {}", system.is_admissible());

    section("Result");
    println!("The violated constraint exists only at the higher organizational level.");
}
