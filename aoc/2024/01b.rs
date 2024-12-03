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

    for i in a {
        for j in &b {
            if i == *j {
                sum += i
            }
        }
    }
    println!("{}", sum);
}
