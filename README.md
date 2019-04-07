# Price Formatter

The script receives a price and outputs it in formatted form

# Quickstart

Python 3 should be already installed.
The price to format is specified when running after the script name.
Also you can specify an optional argument _--precision_ (_-p_). Its default value is _2_.

```bash
$ python format_price.py 1234567.890123 -p 0
1 234 568
```

# Using in other apps

For using _Price Formatter_ in your own apps import function format_price() from format_price.py

```bash
from format_price import format_price

# your code
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
