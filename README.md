Arithmetic Formatter
-------------------
Overview

This Python project formats a list of arithmetic problems vertically and side-by-side, optionally displaying the solutions. It handles addition and subtraction, validates input, and ensures neat alignment.

Features
---------

1.) Supports up to 5 arithmetic problems at a time

2.) Handles only + and - operators

3.) Validates numbers (digits only, max 4 digits)

4.) Outputs neatly formatted vertical display

5.) Optional display of solutions

Usage
-------
Run main.py and provide a list of arithmetic problems. Set show_answers=True to display the results.

## Example

```python
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

print(arithmetic_arranger(problems, True))
```



 ##Sample Output
------------------
```
  32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
  730      3799      88      172
```

Requirements
-------------
Python 3.12 or later


