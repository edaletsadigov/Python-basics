# NumPy Array vs Python List — Performance Comparison

Compares the speed of a vectorized NumPy operation against an equivalent Python `for` loop, using the `timeit` module.

## How It Works

1. Multiplies 1,000,000 numbers by 2 using a Python list comprehension
2. Performs the same operation using a NumPy array (`np.arange()` + vectorized multiplication)
3. Times both approaches with `timeit.timeit()`, averaged over 5 runs
4. Prints the first 5 results from each method and the measured speedup

## Run

```bash
python numpy_vs_list_performance.py
```

## Example Output

```
List nəticəsi (ilk 5): [2, 4, 6, 8, 10]
NumPy nəticəsi (ilk 5): [2 4 6 8 10]

List vaxtı : 0.2341 saniyə
NumPy vaxtı: 0.0023 saniyə
NumPy təxminən 101 dəfə daha sürətlidir.
```

## Why It Matters

This is a direct, measured demonstration of why vectorized operations are preferred over explicit loops when working with large arrays — a core principle behind using NumPy and pandas for data analysis instead of plain Python loops.

## Requirements

```bash
pip install numpy
```

Python 3.x with NumPy. `timeit` is part of the standard library.
