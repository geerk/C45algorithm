import unittest
from c45 import *


class TestC45(unittest.TestCase):

    def setUp(self):
        self.table = json.loads(open('table.json').read())

    def test_freq(self):
        self.assertEquals(freq(self.table, 'arg1', 'left'), 2)
        self.assertEquals(freq(self.table, 'result', 'no'), 2)
        self.assertEquals(freq(self.table, 'arg3', 'foo'), 0)

    def test_info(self):
        self.assertEquals(info(self.table, 'result'), 1)

    def test_infox(self):
        self.assertEquals(infox(self.table, 'arg1', 'result'), 1)

    def test_gain(self):
        self.assertEquals(gain(self.table, 'arg1', 'result'), 0)


if __name__ == '__main__':
    unittest.main()
