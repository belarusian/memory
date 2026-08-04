use continuation_shared::{banner, section};

#[derive(Debug, Clone, Copy, PartialEq)]
enum Status { Active, Refused }

#[derive(Debug)]
struct Branch {
    parent: Option<usize>,
    value: i32,
    status: Status,
}

fn main() {
    banner("Branch Persistence",
        "Preserved alternatives make recovery a reactivation rather than reconstruction.");

    let mut branches = vec![
        Branch { parent: None, value: 0, status: Status::Refused },
        Branch { parent: Some(0), value: 4, status: Status::Active },
        Branch { parent: Some(0), value: -2, status: Status::Refused },
    ];

    section("Failure");
    branches[1].status = Status::Refused;
    println!("active branch became inadmissible");

    section("Recovery");
    branches[2].status = Status::Active;
    println!("reactivated branch: {:?}", branches[2]);
    println!("parent preserved: {:?}", branches[2].parent);
    println!(
        "recovered value {} required no re-derivation, only re-activation of status",
        branches[2].value
    );

    section("History");
    println!("{branches:#?}");
}
