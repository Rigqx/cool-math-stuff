import mpmath
from multiprocessing import Pool

# Function to calculate π using the Leibniz formula for π with arbitrary precision
def calculate_pi_leibniz(n):
    mpmath.mp.dps = n  # Set the number of decimal places (precision)
    pi_approximation = mpmath.mpf(0)
    for k in range(n):
        pi_approximation += ((-1) ** k) / (2 * k + 1)
    return 4 * pi_approximation

# Function to calculate π using multi-core processing
def calculate_pi_with_multiprocessing(precision):
    num_cores = 4  # Set the number of CPU cores to use (adjust as needed)
    with Pool(num_cores) as pool:
        results = pool.map(calculate_pi_leibniz, [precision] * num_cores)
    pi_approximation = sum(results) / num_cores
    return pi_approximation

if __name__ == '__main__':
    # Adjust the precision for your desired level of accuracy (number of decimal places)
    precision = 10000000

    # Calculate π approximation using multi-core processing with mpmath
    approximation = calculate_pi_with_multiprocessing(precision)

    print(f"Approximation of π using {precision} decimal places: {approximation}")
