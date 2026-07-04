# Palindrome Checker

Checks whether a word or phrase reads the same forwards and backwards.

## How it works

1. User enters a word or phrase
2. Script lowercases it and removes spaces
3. Compares the result with its reverse using slicing (`[::-1]`)

## Run

```bash
python palindrome_checker.py
```

## Example

```
Enter a word or phrase: racecar
"racecar" is a palindrome ✓

Enter a word or phrase: hello
"hello" is not a palindrome ✗
```

## Requirements

Python 3.x — no external libraries needed.
