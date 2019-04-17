import argparse
import sys


def get_args():
    parser = argparse.ArgumentParser(
        description='The app outputs a price in formatted form')
    parser.add_argument('price', help='a price to format')
    parser.add_argument(
        '--precision',
        '-p',
        help='precision for rounding',
        type=int
    )

    args = parser.parse_args()
    return [args.price, args.precision]


def format_price(price, precision=2):
    if price is None:
        return
    try:
        if isinstance(price, str):
            price = price.replace(',', '.').replace(' ', '')
        return '{0:,.{1}f}'.format(
            float(price),
            precision,
        ).replace(',', ' ').replace('.00', '')
    except ValueError:
        return


if __name__ == '__main__':
    not_formatted_price, precision = get_args()
    formatted_price = format_price(not_formatted_price, precision)
    if formatted_price is None:
        sys.exit("Price can't be output")
    print(formatted_price)
