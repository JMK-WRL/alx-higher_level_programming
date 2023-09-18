#!/usr/bin/python3
import unittest
import json
import inspect

from models.base import Base
from models.square import Square


class TestBase(unittest.TestCase):

    def test_id_none(self):
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        b = Base((8,))
        self.assertEqual((8,), b.id)

    def test_to_json_type(self):
        sq = Square(1)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string), [{"id": 609, "y": 0, "size": 1, "x": 0}])

    def test_to_json_None(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        sq = Square(1, 0, 0, 609)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)


if __name__ == '__main__':
    unittest.main()
