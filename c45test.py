import unittest
import json

from c45 import freq, info, infox, gain


class TestC45(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('table.json') as f:
            cls.table = json.loads(f.read())

    def test_freq(self):
        self.assertEqual(freq(self.table, 'arg1', 'left'), 2)
        self.assertEqual(freq(self.table, 'result', 'no'), 2)
        self.assertEqual(freq(self.table, 'arg3', 'foo'), 0)

    def test_info(self):
        self.assertEqual(info(self.table, 'result'), 1)

    def test_infox(self):
        self.assertEqual(infox(self.table, 'arg1', 'result'), 1)

    def test_gain(self):
        self.assertEqual(gain(self.table, 'arg1', 'result'), 0)


if __name__ == '__main__':
    unittest.main()
