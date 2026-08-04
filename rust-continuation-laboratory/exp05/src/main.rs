use continuation_shared::{banner, section};

struct ReadCapability<'a, T>(&'a T);
struct WriteCapability<'a, T>(&'a mut T);
struct TransferCapability<T>(T);

fn inspect(cap: ReadCapability<'_, i32>) { println!("observed {}", cap.0); }
fn revise(cap: WriteCapability<'_, i32>) { *cap.0 += 1; }
fn relay(cap: TransferCapability<String>) -> String { cap.0 }

fn main() {
    banner("Authority Without Knowledge",
        "Knowing a value and being authorized to alter or transfer it are different.");

    let mut number = 41;
    section("Capabilities");
    inspect(ReadCapability(&number));
    revise(WriteCapability(&mut number));
    println!("after write authority: {number}");

    let secret = String::from("sealed payload");
    let secret = relay(TransferCapability(secret));
    println!("transferred without semantic inspection: {} bytes", secret.len());

    section("Result");
    println!("Capabilities partition operations that ordinary possession tends to conflate.");
}
