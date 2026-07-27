import numpy as np
import timeit


def multiply_list(n):
    return [x * 2 for x in range(n)]


def multiply_numpy(n):
    return np.arange(n) * 2


def format_time(seconds):
    return f"{seconds:.4f}"


def main():
    n = 1_000_000
    list_neticesi = multiply_list(n)
    numpy_neticesi = multiply_numpy(n)

    print(f"List nəticəsi (ilk 5): {list_neticesi[:5]}")
    print(f"NumPy nəticəsi (ilk 5): {numpy_neticesi[:5]}")

    number = 5
    vaxt_list = timeit.timeit(lambda: multiply_list(n), number=number)
    vaxt_numpy = timeit.timeit(lambda: multiply_numpy(n), number=number)

    avg_list = vaxt_list / number
    avg_numpy = vaxt_numpy / number
    speedup = avg_list / avg_numpy if avg_numpy else float("inf")

    print(f"\nList vaxtı : {format_time(avg_list)} saniyə")
    print(f"NumPy vaxtı: {format_time(avg_numpy)} saniyə")
    print(f"NumPy təxminən {speedup:.0f} dəfə daha sürətlidir.")


if __name__ == "__main__":
    main()

