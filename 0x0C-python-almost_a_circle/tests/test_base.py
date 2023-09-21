import unittest
import pycodestyle
from base import Base, Rectangle, Square  # Import the classes from base.py


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # This method is run once before all the tests
        pass

    @classmethod
    def tearDownClass(cls):
        # This method is run once after all the tests
        pass

    def setUp(self):
        # This method is run before each test
        pass

    def tearDown(self):
        # This method is run after each test
        pass

    def test_constructor_with_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_with_dicts(self):
        # Create some dictionaries to test
        dicts = [{"a": 1, "b": 2}, {"x": 10, "y": 20}]
        result = Base.to_json_string(dicts)
        expected = '[{"a": 1, "b": 2}, {"x": 10, "y": 20}]'
        self.assertEqual(result, expected)

    def test_save_to_file(self):
        # Create some instances of Rectangle and Square to test
        r1 = Rectangle(10, 20)
        r2 = Rectangle(5, 5)
        s1 = Square(4)
        s2 = Square(8)

        # Save instances to a file
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1, s2])

        # Read the file content and check if it matches the expected JSON
        with open("Rectangle.json", "r") as file:
            rect_json = file.read()
        with open("Square.json", "r") as file:
            square_json = file.read()

        self.assertEqual(rect_json, '[{"id": 1, "width": 10, "height": 20}, {"id": 2, "width": 5, "height": 5}]')
        self.assertEqual(square_json, '[{"id": 1, "size": 4}, {"id": 2, "size": 8}]')

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_with_json(self):
        json_str = '[{"a": 1, "b": 2}, {"x": 10, "y": 20}]'
        result = Base.from_json_string(json_str)
        expected = [{"a": 1, "b": 2}, {"x": 10, "y": 20}]
        self.assertEqual(result, expected)

    def test_create_rectangle(self):
        # Create a dictionary representing a Rectangle
        rect_dict = {"id": 3, "width": 30, "height": 40}
        r = Rectangle.create(**rect_dict)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 3)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)

    def test_create_square(self):
        # Create a dictionary representing a Square
        square_dict = {"id": 4, "size": 5}
        s = Square.create(**square_dict)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 4)
        self.assertEqual(s.size, 5)

    def test_update_with_args(self):
        r = Rectangle(10, 20)
        r.update(1, 15, 25, 35)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 35)

    def test_update_with_kwargs(self):
        r = Rectangle(10, 20)
        r.update(id=2, width=30, height=40, x=50)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 30)
        self.assertEqual(r.height, 40)
        self.assertEqual(r.x, 50)

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 30, 40)
        r_dict = r.to_dictionary()
        expected = {"id": 1, "width": 10, "height": 20, "x": 30, "y": 40}
        self.assertEqual(r_dict, expected)

    def test_load_from_file(self):
        # Create some instances and save them to files
        r1 = Rectangle(10, 20)
        r2 = Rectangle(5, 5)
        s1 = Square(4)
        s2 = Square(8)
        Rectangle.save_to_file([r1, r2])
        Square.save_to_file([s1, s2])

        # Load instances from files and check their attributes
        loaded_rectangles = Rectangle.load_from_file()
        loaded_squares = Square.load_from_file()

        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_squares[0], Square)


if __name__ == '__main__':
    # Check PEP 8 compliance
    style = pycodestyle.StyleGuide()
    result = style.check_files(['base.py', 'test_base.py'])
    assert result.total_errors == 0, "PEP 8 violations found"

    # Run the tests
    unittest.main()

