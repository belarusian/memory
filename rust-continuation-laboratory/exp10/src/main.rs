use continuation_shared::{banner, section};

#[derive(Debug)]
struct DiagnosticCoordinate {
    subsystem: &'static str,
    variable: &'static str,
    deviation: f64,
    confidence: f64,
}

#[derive(Debug)]
struct RepairWarrant {
    expected_improvement: f64,
    structural_risk: f64,
    uncertainty: f64,
}

impl RepairWarrant {
    fn licensed(&self) -> bool {
        self.expected_improvement > self.structural_risk + self.uncertainty
    }
}

fn main() {
    banner("Diagnostic Coordinates",
        "A precise diagnosis may coexist with insufficient warrant to repair.");

    let diagnosis = DiagnosticCoordinate {
        subsystem: "thermal", variable: "sensor_bias", deviation: 0.8, confidence: 0.99,
    };
    let warrant = RepairWarrant {
        expected_improvement: 0.8, structural_risk: 0.6, uncertainty: 0.4,
    };

    section("Diagnosis");
    println!("{diagnosis:?}");
    println!("subsystem={}, variable={}, deviation={}, confidence={}",
        diagnosis.subsystem, diagnosis.variable, diagnosis.deviation, diagnosis.confidence);

    section("Warrant");
    println!("{warrant:?}");
    println!("repair licensed: {}", warrant.licensed());

    section("Result");
    println!("Epistemic success did not automatically create intervention authority.");
}
