import unittest

from .models import Program


class ProgramTest(unittest.TestCase):
    def check(self, name, expected):
        p = Program()
        p.name = name
        p.id = 1
        url = p.get_absolute_url()
        self.assertEqual(f"/program/{expected}-p1", url)

    def test_canonicalization(self):
        self.check("apostrophe's get stripped", "apostrophes-get-stripped")
        self.check("numbers 99 and letters99 ok", "numbers-99-and-letters99-ok")
        self.check("other;{+=}-[]. gone", "other--gone")
