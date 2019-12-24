"""
unittests for checking tasks from 07-python-for-advanced homework
"""

from task1 import *
from task2 import *
import unittest
import time


class TestMetaClassesTask(unittest.TestCase):
    def setUp(self):
        self.test_unit1 = SiamObj('1', '2', a=1)
        self.test_unit2 = SiamObj('1', '2', a=1)
        self.test_unit3 = SiamObj('2', '2', a=1)

    def test_is_same_object(self):
        self.assertTrue(self.test_unit1 == self.test_unit2)
        self.assertFalse(self.test_unit1 != self.test_unit2)

    def test_if_connect_functional(self):
        self.test_unit3.connect('1', '2', 1).a = 2
        self.assertEqual(
                self.test_unit2.a, 2, "'connect' function is failing"
            )

    def test_if_garbage_collector(self):
        pool = self.test_unit3.pool
        del self.test_unit3
        self.assertEqual(len(pool), 1, "garbage wasn't collected, ")

    def teardown(self):
        self.test_unit1.dispose()
        self.test_unit2.dispose()
        self.test_unit3.dispose()


class TestTimerPropertyTask(unittest.TestCase):
    def setUp(self):
        self.m = Message()
        self.initial = m.msg

    def test_is_property_works(self):
        self.assertTrue(self.initial is m.msg)
        self.assertFalse(self.initial is not m.msg)

    time.sleep(10)

    def test_is_timer_works(self):
        self.assertTrue(self.initial is not m.msg)

    def teardown(self):
        pass


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
