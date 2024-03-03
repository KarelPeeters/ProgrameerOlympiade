fn main() {
    let cases = readint();

    for case in 0..cases {
        let n = readint();
        let a = readints();
        assert_eq!(n, a.len() as i64);

        print!("{}", case+1);
        
        for i in 0..a.len() {
            let c = a[i];
            let lt = a[i+1..].iter().filter(|&&x| x <= c).count();

            print!(" {}", lt);
        }

        println!();
    }
}

#[allow(unused)]
fn readline() -> String {
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();
    input.trim().to_string()
}

#[allow(unused)]
fn readint() -> i64 {
    readline().parse().unwrap()
}

#[allow(unused)]
fn readints() -> Vec<i64> {
    readline()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect()
}
