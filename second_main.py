import time
import multiprocessing

def factorize(*numbers):
    results = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        results.append(factors)
    return results

def factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(*numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(factorize_number, numbers)
    return results

if __name__ == "__main__": # я забув про це і подумав що нічого страшного не буде але потім погнало багато помилок і мій пк почав дуже сильно гудіти я зразу офнув візал студіо .....
    numbers = [128, 255, 99999, 10651060]

    start_time = time.time()
    results_sync = factorize(*numbers)
    end_time = time.time()
    print(f"Синхронне виконання: {end_time - start_time:.2f} секунд")
    print(results_sync)

    start_time = time.time()
    results_parallel = factorize_parallel(*numbers)
    end_time = time.time()
    print(f"Паралельне виконання: {end_time - start_time:.2f} секунд")
    print(results_parallel)
