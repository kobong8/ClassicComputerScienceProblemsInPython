import time


def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    v_pi: float = 0.0
    for _ in range(n_terms):
        v_pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return v_pi


if __name__ == "__main__":
    start = time.time()
    print(calculate_pi(1000000))
    end = time.time()

    print(f"Elapsed time : {(end - start)*1000}ms")
