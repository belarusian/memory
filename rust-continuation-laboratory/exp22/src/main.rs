use continuation_shared::{banner, bool_word, section};

#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
enum Shape {
    Circle,
    Square,
    Triangle,
    Hexagon,
}

#[derive(Debug, Clone, Copy)]
struct State {
    shape: Shape,
    value: f64,
}

/// A morphism is defined only between two specific shapes, and is invertible
/// exactly where it is defined. It is not a global symmetry: most pairs of
/// shapes have no morphism connecting them at all.
struct Morphism {
    from: Shape,
    to: Shape,
    apply: fn(f64) -> f64,
    invert: fn(f64) -> f64,
}

fn registry() -> Vec<Morphism> {
    vec![
        Morphism { from: Shape::Circle, to: Shape::Square, apply: |v| v * 2.0, invert: |v| v / 2.0 },
        Morphism { from: Shape::Square, to: Shape::Circle, apply: |v| v / 2.0, invert: |v| v * 2.0 },
        Morphism { from: Shape::Square, to: Shape::Triangle, apply: |v| v + 3.0, invert: |v| v - 3.0 },
        Morphism { from: Shape::Triangle, to: Shape::Square, apply: |v| v - 3.0, invert: |v| v + 3.0 },
    ]
}

fn direct(reg: &[Morphism], from: Shape, to: Shape) -> Option<&Morphism> {
    reg.iter().find(|m| m.from == from && m.to == to)
}

/// Composition: a path of length at most two through the registry. This is
/// how groupoid morphisms combine — only when their endpoints line up.
fn repair(reg: &[Morphism], state: State, target: Shape) -> Option<State> {
    if state.shape == target {
        return Some(state);
    }
    if let Some(m) = direct(reg, state.shape, target) {
        return Some(State { shape: target, value: (m.apply)(state.value) });
    }
    for mid in reg.iter().map(|m| m.to) {
        if let (Some(first), Some(second)) =
            (direct(reg, state.shape, mid), direct(reg, mid, target))
        {
            let mid_value = (first.apply)(state.value);
            return Some(State { shape: target, value: (second.apply)(mid_value) });
        }
    }
    None
}

fn main() {
    banner(
        "Repair Groupoid",
        "Repairs compose like a groupoid, not a group: invertible where defined, but not universally connecting.",
    );

    let reg = registry();
    let origin = State { shape: Shape::Circle, value: 5.0 };

    section("Direct repair");
    let to_square = repair(&reg, origin, Shape::Square).unwrap();
    println!("circle(5.0) repaired to square: {to_square:?}");

    section("Composed repair");
    let to_triangle = repair(&reg, origin, Shape::Triangle);
    println!("circle(5.0) repaired to triangle via square: {to_triangle:?}");

    section("Undefined repair");
    let to_hexagon = repair(&reg, origin, Shape::Hexagon);
    println!(
        "circle(5.0) repaired to hexagon: {} (no morphism, and no chain of morphisms, connects them)",
        bool_word(to_hexagon.is_some())
    );

    section("Invertibility where defined");
    let m = direct(&reg, Shape::Circle, Shape::Square).unwrap();
    let forward = (m.apply)(origin.value);
    let back = (m.invert)(forward);
    println!("circle->square->circle: {} -> {forward} -> {back}", origin.value);
    println!(
        "round trip recovers origin exactly: {}",
        bool_word((back - origin.value).abs() < f64::EPSILON)
    );

    section("Result");
    println!("Every defined morphism is invertible on its own domain, so local repair never loses information.");
    println!("But invertibility of each arrow does not add up to a single symmetry linking every state to every other.");
    println!("A group would guarantee Hexagon is reachable from Circle; this groupoid does not, because no such repair was ever admissible to begin with.");
}
