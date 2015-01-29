import unittest
from objectid import ObjectId


class TestConnection(unittest.TestCase):
    def test_assemble(self):
        f = ObjectId()
        self.assertEquals(len(f._id), 24)
        self.assertIsInstance(f.time, int)

    def test_disassemble(self):
        o = ObjectId('5307236762e2167d348b456b')
        self.assertEquals(o.time, 1392976743)

    def test_operator(self):
        a = ObjectId()
        b = ObjectId()
        self.assertTrue(b > a)
        self.assertTrue(a < b)
        self.assertTrue(a != b)
        self.assertTrue(a == ObjectId(str(a)))
        self.assertTrue(a >= ObjectId(str(a)))
        self.assertTrue(a <= ObjectId(str(a)))
