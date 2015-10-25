import json
import unittest
import utils


class TestDataMinig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open('table.json') as f:
            cls.table = json.loads(f.read())

    def test_is_mono(self):
        testlist = ['yes', 'yes', 'yes', 'yes']
        self.assertTrue(utils.is_mono(testlist))
        testlist = ['yes', 'no', 'yes', 'yes']
        self.assertFalse(utils.is_mono(testlist))

    def test_deldup(self):
        testlist = ['yes', 'yes', 'yes', 'yes']
        self.assertEqual(utils.deldup(testlist), ['yes'])
        testlist = ['yes', 'no', 'yes', 'no']
        self.assertEqual(utils.deldup(testlist), ['yes', 'no'])

    def test_get_indexes(self):
        self.assertEqual(utils.get_indexes(self.table, 'arg3', 'no'), [0, 3])
        self.assertEqual(utils.get_indexes(self.table, 'arg3', 'dunno'), [])
        self.assertEqual(utils.get_indexes(self.table, 'arg2', 'down'),
                         [0, 2, 3])

    def test_get_values(self):
        self.assertEqual(utils.get_values(self.table, 'arg1', [0, 2, 3]),
                         ['left', 'right', 'right'])
        self.assertEqual(utils.get_values(self.table, 'arg3', [1, 3]),
                         ['yes', 'no'])
        self.assertEqual(utils.get_values(self.table, 'arg1', []), [])
        self.assertEqual(utils.get_values(self.table, 'arg1', [9, 12]), [])

    def test_del_values(self):
        expected = {
            'result': ['yes', 'yes'],
            'arg1': ['left', 'right'],
            'arg2': ['down', 'down'],
            'arg3': ['no', 'yes'],
        }
        self.assertEqual(utils.del_values(self.table, [0, 2]), expected)
        expected = {
            'result': [],
            'arg1': [],
            'arg2': [],
            'arg3': [],
        }
        self.assertEqual(utils.del_values(self.table, []), expected)
        expected = {
            'result': ['yes', 'yes', 'no'],
            'arg1': ['left', 'right', 'right'],
            'arg2': ['down', 'down', 'down'],
            'arg3': ['no', 'yes', 'no'],
        }
        self.assertEqual(utils.del_values(self.table, [0, 2, 3]), expected)

    def test_get_subtables(self):
        expected = [
        {   'result': ['yes', 'no'],
            'arg1': ['left', 'left'],
            'arg2': ['down', 'up'],
            'arg3': ['no', 'yes'],
        },
        {   'result': ['yes', 'no'],
            'arg1': ['right', 'right'],
            'arg2': ['down', 'down'],
            'arg3': ['yes', 'no'],
        }]
        self.assertEqual(utils.get_subtables(self.table, 'arg1'), expected)



if __name__ == '__main__':
    unittest.main()
