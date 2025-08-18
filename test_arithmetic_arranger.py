import unittest
from arithmetic_arranger import arithmetic_arranger


class TestArithmeticArranger(unittest.TestCase):

    def test_arrangement_without_answers(self):
        problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
        expected = (
            "   32      3801      45      123\n"
            "+ 698    -    2    + 43    +  49\n"
            "-----    ------    ----    -----"
        )
        self.assertEqual(arithmetic_arranger(problems), expected)

    def test_arrangement_with_answers(self):
        problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
        expected = (
            "   32      3801      45      123\n"
            "+ 698    -    2    + 43    +  49\n"
            "-----    ------    ----    -----\n"
            "  730      3799      88      172"
        )
        self.assertEqual(arithmetic_arranger(problems, True), expected)

    def test_too_many_problems(self):
        problems = ["32 + 8", "1 - 2", "45 + 43", "123 + 49", "9999 + 1", "10 + 10"]
        self.assertEqual(arithmetic_arranger(problems), "Error: Too many problems.")

    def test_invalid_operator(self):
        problems = ["32 * 698", "1 - 2"]
        self.assertEqual(arithmetic_arranger(problems), "Error: Operator must be '+' or '-'.")

    def test_non_digit(self):
        problems = ["32 + ab", "1 - 2"]
        self.assertEqual(arithmetic_arranger(problems), "Error: Numbers must only contain digits.")

    def test_too_long_number(self):
        problems = ["12345 + 1", "1 - 2"]
        self.assertEqual(arithmetic_arranger(problems), "Error: Numbers cannot be more than four digits.")


if __name__ == "__main__":
    unittest.main()

