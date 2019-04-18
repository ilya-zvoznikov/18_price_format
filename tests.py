import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_price_is_none(self):
        fp = format_price(None)
        self.assertIsNone(fp)

    def test_price_is_zero(self):
        fp = format_price(0)
        self.assertEqual(fp, '0')

    def test_price_is_almost_zero(self):
        fp = format_price(0.00000001)
        self.assertEqual(fp, '0')

    def test_price_is_str_zero(self):
        fp = format_price('0')
        self.assertEqual(fp, '0')

    def test_whole_number(self):
        fp = format_price(1234567)
        self.assertEqual(fp, '1 234 567')

    def test_float_number(self):
        fp = format_price(3245.659884)
        self.assertEqual(fp, '3 245.66')

    def test_negative_number(self):
        fp = format_price(-1234)
        self.assertEqual(fp, '-1 234')

    def test_string_with_dot(self):
        fp = format_price('3245.376473')
        self.assertEqual(fp, '3 245.38')

    def test_string_with_comma(self):
        fp = format_price('3245,873473')
        self.assertEqual(fp, '3 245.87')

    def test_string_with_space(self):
        fp = format_price('3 453.432')
        self.assertEqual(fp, '3 453.43')

    def test_string_with_neg_number(self):
        fp = format_price('-2345.654')
        self.assertEqual(fp, '-2 345.65')

    def test_string_with_letters(self):
        fp = format_price('1234.12d')
        self.assertIsNone(fp)

    def test_precision_is_none(self):
        precision = None
        fp = format_price(3245.659884, precision)
        self.assertIsNone(fp)

    def test_precision_is_int(self):
        precision = 4
        fp = format_price(3245.659884, precision)
        self.assertEqual(fp, '3 245.6599')

    def test_precision_is_int_from_str(self):
        precision = '3'
        fp = format_price(3245.659884, precision)
        self.assertEqual(fp, '3 245.660')

    def test_precision_is_float(self):
        precision = 2.1
        fp = format_price(3245.659884, precision)
        self.assertIsNone(fp)

    def test_precision_is_str(self):
        precision = 'letters'
        fp = format_price(3245.659884, precision)
        self.assertIsNone(fp)

    def test_price_is_bool(self):
        fp = format_price(True)
        self.assertIsNone(fp)

    def test_price_is_list(self):
        fp = format_price([1, 2])
        self.assertIsNone(fp)


if __name__ == '__main__':
    unittest.main()
