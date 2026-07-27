# Practice 2 — Data Types Deep Dive

A more detailed follow-up to Practice 1, organized by data type: numbers, strings, booleans, lists, dictionaries, tuples, and sets.

## Topics Covered

**Numbers** — arithmetic between `int` and `float`, type conversion, checking the resulting type after an operation.

**Strings** — extracting a word from a sentence using several different approaches (`find()`, `split()` + indexing, `split()` + `.index()`), replacing words inside a split list, f-string formatting, and controlling decimal precision (`.1f`, `.2f`, `.3f`).

**Booleans** — declaring and assigning boolean variables.

**Lists** — sorting, appending vs. extending (and why `extend()` is needed instead of `append()` when adding a value that shouldn't be split into characters), removing elements by value and by index, inserting into a sorted list.

**Dictionaries** — reading keys and values, updating a value by key, retrieving a value by key.

**Tuples** — accessing first/last elements, removing an element (via conversion to list, since tuples are immutable).

**Sets** — creating a set from a tuple, adding an element, counting elements.

## Notes

Several string exercises include multiple solution attempts with comments explaining the reasoning behind each approach — for example, choosing a dynamic method to find a word's position instead of hardcoding it, so the code still works if the sentence changes.

## Run

Open in Jupyter Notebook or Google Colab and run cells sequentially. No external libraries required beyond the Python standard library.

## Requirements

Python 3.x
