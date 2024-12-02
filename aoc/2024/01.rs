fn main() {
    let mut sum = 0;
    let mut a: Vec<isize> = vec![];
    let mut b: Vec<isize> = vec![];
    let data = std::fs::read_to_string("aoc/2024/01.txt").unwrap();

    for line in data.split("\n") {
        let ab: Vec<&str> = line.split("   ").collect();
        a.append(&mut vec![ab[0].parse::<isize>().unwrap()]);
        b.append(&mut vec![ab[1].parse::<isize>().unwrap()]);
    }

    a.sort();
    b.sort();

    for i in 0..a.len() {
        sum += (a[i] - b[i]).abs();
    }
    println!("{}", sum);
}
