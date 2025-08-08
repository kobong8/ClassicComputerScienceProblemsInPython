fn calculate_pi(n_terms: usize) -> f64 {
    let numerator: f64 = 4.0;
    let mut denominator: f64 = 1.0;
    let mut operation: f64 = 1.0;
    let mut v_pi: f64 = 0.0;

    for _ in 0..n_terms {
        v_pi += operation * (numerator / denominator);
        denominator += 2.0;
        operation *= -1.0;
    }

    v_pi
}

fn main() {
    println!("{}", calculate_pi(1_000_000));
}