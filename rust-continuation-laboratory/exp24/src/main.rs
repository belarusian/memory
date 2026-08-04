use continuation_shared::{banner, bool_word, section};

/// Two observers see the same corrupted array. One also kept a parity
/// channel from before the corruption; the other did not. Restorability is
/// not a property of the corrupted object alone.
struct Observer {
    name: &'static str,
    parity: Option<u8>,
}

impl Observer {
    fn try_restore(&self, corrupted: &[u8], missing_index: usize) -> Option<u8> {
        let parity = self.parity?;
        let known_xor = corrupted
            .iter()
            .enumerate()
            .filter(|(i, _)| *i != missing_index)
            .fold(0u8, |acc, (_, b)| acc ^ b);
        Some(parity ^ known_xor)
    }
}

fn main() {
    banner(
        "Observer-Relative Restorability",
        "The same corrupted object is restorable through one interface and not through another; restorability is a relation, not a property of the object alone.",
    );

    let original: [u8; 5] = [12, 200, 7, 91, 33];
    let parity_channel: u8 = original.iter().fold(0u8, |acc, b| acc ^ b);

    section("Corruption");
    let missing_index = 2;
    let mut corrupted = original;
    corrupted[missing_index] = 0;
    println!("original: {original:?}");
    println!("corrupted (index {missing_index} zeroed): {corrupted:?}");
    println!("both observers see exactly this corrupted array, byte for byte");

    let with_parity = Observer { name: "kept a parity channel", parity: Some(parity_channel) };
    let without_parity = Observer { name: "kept no side channel", parity: None };

    section("Restoration attempts");
    for observer in [&with_parity, &without_parity] {
        let restored = observer.try_restore(&corrupted, missing_index);
        match restored {
            Some(value) => println!(
                "observer who {}: restored missing byte = {value} (correct: {})",
                observer.name,
                bool_word(value == original[missing_index])
            ),
            None => println!(
                "observer who {}: cannot restore, no channel to draw on",
                observer.name
            ),
        }
    }

    section("Result");
    println!("The corrupted array itself is identical for both observers.");
    println!("Restorability differed entirely because of what each observer had preserved before the corruption occurred, not because of anything in the corrupted state.");
}
