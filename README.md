# Phone Search

A small Python program that finds a person's name from their phone number.

Type a 10-digit number and the program prints the name it belongs to.

## How it works

The program keeps a dictionary of names and phone numbers. When you type a number, it looks for it in the dictionary and prints the matching name.

- If the number is not exactly 10 digits, it asks again.
- If you type letters instead of numbers, it asks again.
- If the number is not in the dictionary, it prints `Number not found`.

## Requirements

- Python 3.8 or newer

No extra libraries are needed.

## Usage

Run the program:

```
python phone_search.py
```

Example:

```
Just put the number and you will get the name AUTO ::: 1111111111
1111111111 of Ghala
Just put the number and you will get the name AUTO ::: 11111111111
!!!! we accept only 10 digits !!!!
Just put the number and you will get the name AUTO ::: abc
!!!! We accept only numbers !!!!
Just put the number and you will get the name AUTO ::: 9999999999
Number not found
```

The program keeps asking for numbers. Press `Ctrl + C` to stop it.

## Adding or changing numbers

Open `phone_search.py` and edit the dictionary in the `phone()` function:

```python
numbers = {
    'Ghala' : 1111111111,
    'Ahmed' : 2222222222,
    'Ali' : 3333333333,
    'Mohammed' : 4444444444
}
```

Each number must have exactly 10 digits.

## Functions

| Function | What it does |
|---|---|
| `main()` | Asks for a number, checks it, and shows the result |
| `phone()` | Returns the dictionary of names and numbers |
| `search(number)` | Returns the position of the number in the dictionary, or `None` if it is not there |
| `get_name(number)` | Prints the name for the number, or `Number not found` |

## Tests

Run the tests:

```
python test_phone_search.py
```

If everything works, it prints `All tests passed`.

## Files

- `phone_search.py` - the program
- `test_phone_search.py` - the tests
- `README.md` - this file
