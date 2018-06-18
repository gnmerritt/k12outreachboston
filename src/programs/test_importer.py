import unittest

from programs.importer import split_dicts, extract_dict


class TestRowExtractor(unittest.TestCase):
    dict = {'A.foo': 'A', 'B.bar': 'B'}

    def test_extract_rows(self):
        a = extract_dict('A', self.dict)
        self.assertEqual(a, {'foo': 'A'})

        b = extract_dict('B.', self.dict)
        self.assertEqual(b, {'bar': 'B'})

        self.assertEqual(extract_dict("missing", self.dict), {})

    def test_split(self):
        a, b = split_dicts(self.dict, ['A', 'B'])
        self.assertEqual(a, {'foo': 'A'})
        self.assertEqual(b, {'bar': 'B'})
