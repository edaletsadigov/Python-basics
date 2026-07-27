# NumPy Practice

Introductory exercises with NumPy arrays: creation, boolean masking, filtering, and conditional replacement.

## Topics Covered

- Creating arrays with `np.arange()` and checking the NumPy version
- Creating a boolean array with `np.ones()` and `np.full()`, and comparing the two approaches
- Filtering odd numbers from an array using boolean indexing, tested with three different conditions (`x % 2 > 0`, `!= 0`, `np.mod()`)
- Replacing odd values in-place with `-1`
- Combining conditions with `&` to filter positive even numbers
- Slicing with a step (`arr[::2]`) to extract elements at even indices and sum them
- Filtering with `|` (OR) to keep numbers divisible by 5 or 7, compared against an equivalent list comprehension

## Notes

Several exercises are solved more than once with different NumPy methods (e.g. `np.full()` vs `np.ones()`, boolean indexing vs `np.mod()`) to compare readability and confirm they produce the same result.

## Run

Open in Jupyter Notebook or Google Colab and run cells sequentially.

## Requirements

```bash
pip install numpy
```
