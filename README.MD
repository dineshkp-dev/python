# Basic Setup

## Install python

- Go to python download website

```
https://www.python.org/downloads/windows/
```

- Download Windows installer (64bit)
- During installation ensure that 'Add to PATH is selected'
- Ensure python was installed by starting from the Interactive python (REPL - Read Evaluate Print Loop)

```
>> python
Python 3.9.0 (default, Oct 27 2020, 14:15:17)
[Clang 12.0.0 (clang-1200.0.32.21)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>> quit()
```

## Install VS-Code

- Download VSCode from the website below

```
https://code.visualstudio.com/download
```

- Download Windows 64bit Use Installer

# Python Basics

## Python Interactive

- Open the command line and type the following in the python interactive console

```
python3
>>> 2 + 2
4
>>> 6 * 7
42
>>> x = 5 # assignment
# assign value of 5 to a variable called 'x'
>>> x
5
>>> 5 * x
25
>>> _
25
>>> _ * 2
50
>>> _
50
>>> 6*5
30
>>> _
30
>>> print('Hello world')
>>> y = dinesh
>>> for i in range(5):
...     print('my name is ' + y)
...

>>>quit()
```

- NOTE: \_ retains the value of the previous evaluation

## Python Standard library

- Using the import keyword

```
>>> import datetime
>>> today = datetime.date.today()
>>> today
datetime.date(2021, 1, 3)
```

- Getting to know other attributes to use: help(module_name)

```
help(datetime)
```

- Importing a specific function from a module
  - from module_name import function

```
>>> from datetime import date
>>> date.today()
datetime.date(2021, 1, 3)
>>>

```

- Importing a specific function from a module and assigning a variable name to it
  - from module_name import function as variable

```
>>> from datetime import date as d
>>> d.today()
datetime.date(2021, 1, 3)
>>>

```

# Types

- int
  - eg. 1, 2, 3, 4
  - unlimited precision signed integers

```
>>> 0b10 # binary
2
>>> 0o10 # octal
8
>>> 0x10 # hexadecimal
16
>>> int("456")
456
```

- float
  - eg. 1.2, 1.3, 1.4
  - 15-16 significant digits in decimal

```
>>> 1.2345
1.2345
>>> float("1.2345")
1.2345
>>> float("nan")
nan
>>> 3.0 + 1
4.0
```

- NoneType
  - None

```
>>> None
>>> x = None
>>> x is not None
False
>>> x is None # checking if variable is None using the 'is' operator
True
```

- boolean
  - bool True
  - bool False

```
>>> bool(0)
False
>>> bool(1)
True
>>> bool(123)
True
>>> bool([])
False
>>> bool([1,2,3])
True
>>> bool("")
False
>>> bool("dinesh")
True
>>> bool(x)
False
>>> x
>>> x = 'dinesh'
>>> bool(x)
True
```

- Relational operators
  - == equality/is equal
  - != is not equal
  - <> is not equal
  - < less than
  - \> greater than
  - <= less than or equal
  - \>= greater than or equal

# References

- Core Python: Getting Started from Pluralsight
- PEP (Python Enhancement Proposals) for python styling - [PEP8](https://www.python.org/dev/peps/pep-0008/)
- [PEP20 - Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- Python Standard Library [Libary](https://docs.python.org/3/library/index.html)
- [Python operators](https://www.tutorialspoint.com/python/python_basic_operators.htm)
