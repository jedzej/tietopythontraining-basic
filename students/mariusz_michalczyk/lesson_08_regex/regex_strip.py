import re
import unittest


def strip_mm(text, replacement=''):
    if not replacement:
        rgx_strip = re.compile(r'^\s*(\d*\w*)\s*$')
        matched = rgx_strip.search(text)
        return matched.group(1)
    else:
        replacement = re.escape(replacement)
        regex = re.compile(r'^[{0}]*|[{0}]*$'.format(replacement))
        return regex.sub("", text)


if __name__ == '__main__':
    user_input = input("Enter yout text: ")
    print(strip_mm(user_input, replacement='t'))


class TestsValidateStrip(unittest.TestCase):

    def test_strip_big_space(self):
        self.assertEqual(
            strip_mm("   odo  "), 'odo')

    def test_strip_right_space(self):
        self.assertEqual(
            strip_mm("odo  "), 'odo')

    def test_strip_two_words_in_text(self):
        self.assertEqual(
            strip_mm("odo rodo", replacement="o"), 'do rod')

    def test_special_char(self):
        self.assertEqual(
            strip_mm(".leon.", replacement="."), 'leon')

    def test_double_special_char(self):
        self.assertEqual(
            strip_mm(".$leon.$", replacement=".$"), 'leon')

    def test_strip_two_chars_replacement_with_space(self):
        self.assertEqual(
            strip_mm("xo takie tam xo", replacement="xo"), ' takie tam ')

    def test_strip_two_chars_replacement_with_space2(self):
        self.assertEqual(
            strip_mm("xo takie tam xo ", replacement="xo "), 'takie tam')
