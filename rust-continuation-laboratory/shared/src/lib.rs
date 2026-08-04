use std::fmt::Debug;

pub trait Admissible {
    fn is_admissible(&self) -> bool;
}

pub trait Perturb {
    type Disturbance;
    fn perturb(&mut self, disturbance: Self::Disturbance);
}

pub trait Repairable {
    type Repair: Clone + Debug;
    fn candidate_repairs(&self) -> Vec<Self::Repair>;
    fn apply_repair(&mut self, repair: &Self::Repair);
}

pub trait Continue: Sized {
    fn successors(&self) -> Vec<Self>;
}

#[derive(Debug, Clone, Copy)]
pub struct Evaluation {
    pub locally_valid: bool,
    pub structurally_valid: bool,
    pub continuation_depth: usize,
    pub repair_cost: f64,
    pub irreversible_risk: f64,
}

pub fn banner(name: &str, claim: &str) {
    println!("EXPERIMENT: {name}");
    println!("CLAIM: {claim}\n");
}

pub fn section(name: &str) {
    println!("\n{name}");
    println!("{}", "-".repeat(name.len()));
}

pub fn bool_word(value: bool) -> &'static str {
    if value { "yes" } else { "no" }
}
