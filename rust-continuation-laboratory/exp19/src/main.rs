use continuation_shared::{banner, section};

#[derive(Debug, Clone, Copy)]
struct Body {
    cytokines: f64,
    temperature: f64,
    heart_rate: f64,
    perfusion: f64,
}

impl Body {
    fn step_coupled(&mut self) {
        let fever_setpoint = 37.0 + self.cytokines * 0.4;
        self.temperature += (fever_setpoint - self.temperature) * 0.3;
        self.heart_rate = 70.0 + (self.temperature - 37.0) * 12.0;
        self.perfusion = 1.0 - ((self.heart_rate - 85.0).max(0.0) / 100.0);
        self.cytokines *= 0.92 + (1.0 - self.perfusion) * 0.08;
    }

    fn admissible(&self) -> bool {
        self.temperature < 41.0 && self.heart_rate < 150.0 && self.perfusion > 0.65
    }
}

fn main() {
    banner("Physiological Coupling",
        "Cross-subsystem relations determine whole-body viability.");

    let mut body = Body { cytokines: 5.0, temperature: 37.0, heart_rate: 70.0, perfusion: 1.0 };
    section("Trajectory");
    for t in 0..12 {
        body.step_coupled();
        println!("t={t:02}: {body:?}, admissible={}", body.admissible());
    }
}
