Arithmetic Formatter
-------------------
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/alwandeally/Arithmetic-Formatter?color=green)](https://github.com/alwandeally/Arithmetic-Formatter/commits/main)
[![Run on Replit](https://img.shields.io/badge/Replit-Run-orange?logo=replit)](https://replit.com/new/github/alwandeally/Arithmetic-Formatter)
-----
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

1. Clone the repository:
   ```bash
   git clone https://github.com/alwandeally/Arithmetic-Formatter.git
   ```

2. Navigate into the project folder:
   ```bash
   cd Arithmetic-Formatter
   ```

3. Run the Python file:
   ```bash
   python main.py
   ```


 Example
 ---------

```python
from arithmetic_arranger import arithmetic_arranger

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

print(arithmetic_arranger(problems, True))
```



 Sample Output
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

License
--------
This project is licensed under the MIT License.
