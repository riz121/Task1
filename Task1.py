import unittest
from middle import look_and_say_middle_two

class TestLookAndSayMiddleTwo(unittest.TestCase):
    def test_example_cases(self):
        self.assertEqual(look_and_say_middle_two(5), "12")  # 111221 -> middle two: 12
        self.assertEqual(look_and_say_middle_two(8), "21")  # 1113213211 -> middle two: 21

    def test_additional_cases(self):
        self.assertEqual(look_and_say_middle_two(4), "21")  # 1211 -> middle two: 21
        self.assertEqual(look_and_say_middle_two(6), "22")  # 312211 -> middle two: 22

if __name__ == "__main__":
    unittest.main()
