# Python for Data Science Piscine

This repository contains various exercises and solutions for the Python for Data Science Piscine. Each exercise is designed to help you understand and master different concepts and techniques in Python programming.

## Table of Contents

- [Exercise 00 - First Python Script](#exercise-00---first-python-script)
- [Exercise 01 - First Use of Package](#exercise-01---first-use-of-package)
- [Exercise 02 - First Function Python](#exercise-02---first-function-python)
- [Exercise 03 - NULL Not Found](#exercise-03---null-not-found)
- [Exercise 04 - The Even and the Odd](#exercise-04---the-even-and-the-odd)
- [Exercise 05 - First Standalone Program Python](#exercise-05---first-standalone-program-python)
- [Exercise 06 - ft_filter](#exercise-06---ft_filter)
- [Exercise 07 - Dictionaries SoS](#exercise-07---dictionaries-sos)
- [Exercise 08 - Loading ...](#exercise-08---loading)
- [Exercise 09 - My First Package Creation](#exercise-09---my-first-package-creation)


## Exercise 00 - First Python Script

### Description
Write a script that prints various greetings.

### Usage
```sh
python3.10 Hello.py
```
----------------------
## Exercise 01 - First Use of Package

### Description
Write a script that formats dates using the time and datetime libraries.

### Usage
```sh
python3.10 format_ft_time.py
```
---------------------
## Exercise 02 - First Function Python

### Description
Write a function that prints the object types and returns 42.

### Usage
```python
python3.10 tester.py
```
---------------------------
## Exercise 03 - NULL Not Found

### Description
Write a function that prints the object type of various 'null' types and returns 0 if successful, 1 otherwise.

### Usage
```python
python3.10 tester.py
```
----------------------------
## Exercise 04 - The Even and the Odd

### Description
Create a script that takes a number as an argument and checks whether it is odd or even.

### Usage
```sh
python3.10 whatis.py 14
```
--------------------------
## Exercise 05 - First Standalone Program Python

### Description
Create a standalone program that takes a string and counts the types of characters in it.

### Usage
```sh
python3.10 building.py "Python 3.0, released in 2008..."
```
---------------------------
## Exercise 06 - ft_filter

### Description
Recode the filter function using list comprehensions and create a program that filters words based on length.
Usage

Test the ft_filter function:

    python3.10 tester.py

the print the __doc__
And should print True  

Test the filterstring.py script:

    python3.10 filterstring.py 'Hello the World' 4

This should print:

    ['Hello', 'World']

Another example:

    python3.10 filterstring.py 'Hello the World' 99

This should print:

    []
----------------------
## Exercise 07 - Dictionaries SoS

### Description
Write a program that encodes a string into Morse Code.

### Usage
```sh
python3.10 sos.py "sos"
```
-------------------------
## Exercise 08 - Loading ...

### Description
Create a function that mimics the tqdm progress bar.

### Usage
```python
python3.10 tester.py
```
--------------------------
## Exercise 09 - My First Package Creation

### Description
Create a Python package and publish it.

### Installation

1. Upgrade the `build` package:
    ```sh
    python3.10 -m pip install --upgrade build
    ```

2. Build the package:
    ```sh
    python3.10 -m build
    ```

3. Install the built package:
    ```sh
    pip install ./dist/ft_package-0.0.1-py3-none-any.whl
    ```

### Usage
To use the package, you can import it and call the `count_in_list` function:
```python
python3 -c "
from ft_package import count_in_list

print(count_in_list(['toto', 'tata', 'toto'], 'toto'))  # Output: 2
print(count_in_list(['toto', 'tata', 'toto'], 'tutu'))  # Output: 0
"
```

### Uninstallation
To uninstall the package, use the following command:
```sh
pip uninstall ft-package
```

### Removing and Clean Up Build Artifacts
```sh
rm -rf build dist ft_package.egg-info
```

