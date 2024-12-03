use std::isize;

fn chk_mov(mov: isize, diff: isize) -> isize {
    if mov < -1 { return -1; }
    if diff == 0 { return -1; }
    if diff.abs() > 3 { return -1; }
    if mov == 3 {
        if diff > 0 {
            return 1;
        } else if diff < 0 {
            return 0;
        } else {
            return 3;
        }
    } else {
        if (diff > 0 && mov == 1) || (diff < 0 && mov == 0) {
            return mov;
        } else {
            return -1;
        }
    }
}

fn main() {
    let mut count: isize = 0;
    let data = std::fs::read_to_string("../aoc/2024/02.txt").unwrap();

    for report in data.split("\n") {
        let levels: Vec<&str> = report.split(' ').collect();
        let mut last: isize = 0;
        let mut mov: isize = 3;

        for current in levels.into_iter().map(|x| x.parse::<isize>().unwrap()) {
            if last == 0 {
                last = current;
                continue;
            } else {
                let diff = current - last;
                mov = chk_mov(mov, diff);
                if mov == -1 { break; }
                last = current;
            }
        }
        if mov == 0 || mov == 1 { count += 1; }
    }
    println!("{count}");
}
