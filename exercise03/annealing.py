import math
import numpy as np
import inspect
import time
import matplotlib.pyplot as plt


def func1(x):
    x1, x2 = x
    return (5 - x1) ** 2 + 5 * (x2 - x1**2) ** 2


def func2(x):
    x1, x2 = x
    return (x1**2 + x2 - 11) ** 2 + (x1 + x2**2 - 7) ** 2


def func3(x):
    x1, x2 = x
    return (
        418.9829 * 2
        - x1 * math.sin(math.sqrt(abs(x1)))
        - x2 * math.sin(math.sqrt(abs(x2)))
    )


def simulated_annealing(
    objective_function, initial_temperature, cooling_rate, max_iterations, max_time
):
    # Initialize the current solution randomly
    current_solution = np.array(
        [np.random.uniform(-10, 10), np.random.uniform(-10, 10)]
    )
    current_value = objective_function(current_solution)

    best_solution = current_solution
    best_value = current_value

    temperature = initial_temperature
    start_time = time.time()

    for iteration in range(max_iterations):
        if time.time() - start_time > max_time:
            break  # If time exceeds max_time

        # Generate a new solution based on neighborhood function
        candidate_solution = current_solution + np.random.uniform(-1, 1, 2)
        candidate_value = objective_function(candidate_solution)

        # If new solution is better, accept it
        if candidate_value < current_value:
            current_solution = candidate_solution
            current_value = candidate_value

            # Update best solution if needed
            if candidate_value < best_value:
                best_solution = candidate_solution
                best_value = candidate_value
        else:
            # Maybe accept worse solution
            delta = candidate_value - current_value
            acceptance_probability = np.exp(-delta / temperature)
            if np.random.rand() < acceptance_probability:
                current_solution = candidate_solution
                current_value = candidate_value

        # Decrease the temperature
        temperature *= cooling_rate

    return best_solution, temperature, current_value


initial_temperature = 1000
cooling_rate = 0.995
max_iterations = 100000
max_time = 5

functions = [func1, func2, func3]

for f in functions:
    best_solution, temp, ener = simulated_annealing(
        f, initial_temperature, cooling_rate, max_iterations, max_time
    )
    source = inspect.getsource(f).split("\n")[2].split("return ")[1]
    print(
        f"Best solution for \033[92m{source}\033[0m found: \nSolution: \033[91m{best_solution}\033[0m\nTemperature: \033[91m{temp}\033[0m\nEnergy: \033[91m{ener}\033[0m\n"
    )
