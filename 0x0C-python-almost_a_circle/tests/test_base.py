#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_init(self):
        # Test that instances have unique IDs
        base1 = Base()
        base2 = Base()
        self.assertNotEqual(base1.id, base2.id)

        # Test that instances have the correct ID when provided
        base3 = Base(100)
        self.assertEqual(base3.id, 100)

    def test_to_json_string(self):
        # Test when the input list is empty
        self.assertEqual(Base.to_json_string([]), "[]")

        # Test when the input list is not empty
        data = [{'key': 'value'}, {'key2': 'value2'}]
        json_string = Base.to_json_string(data)
        self.assertEqual(json_string, '[{"key": "value"}, {"key2": "value2"}]')

    def test_save_to_file(self):
        # Test saving an empty list
        Base.save_to_file([])
        with open('Base.json', 'r') as file:
            self.assertEqual(file.read(), '[]')

        # Test saving a list of dictionaries
        data = [{'key': 'value'}, {'key2': 'value2'}]
        Base.save_to_file(data)
        with open('Base.json', 'r') as file:
            self.assertEqual(file.read(), '[{"key": "value"}, {"key2": "value2"}]')

    def test_from_json_string(self):
        # Test when the input JSON string is empty
        self.assertEqual(Base.from_json_string(""), [])

        # Test when the input JSON string is not empty
        json_string = '[{"key": "value"}, {"key2": "value2"}]'
        data = Base.from_json_string(json_string)
        self.assertEqual(data, [{'key': 'value'}, {'key2': 'value2'}])

    def test_create(self):
        # Test creating a Rectangle instance from a dictionary
        rectangle_dict = {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5}
        rectangle = Base.create(**rectangle_dict)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

        # Test creating a Square instance from a dictionary
        square_dict = {'id': 6, 'size': 7, 'x': 8, 'y': 9}
        square = Base.create(**square_dict)
        self.assertEqual(square.id, 6)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_load_from_file(self):
        # Test loading from a non-existent file
        self.assertEqual(Base.load_from_file(), [])

        # Test loading from an existing file
        data = [{'key': 'value'}, {'key2': 'value2'}]
        Base.save_to_file(data)
        loaded_data = Base.load_from_file()
        self.assertEqual(loaded_data, data)

if __name__ == '__main__':
    unittest.main()
