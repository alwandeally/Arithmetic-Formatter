from arithmetic_arranger import arithmetic_arranger

def run_tests():
    tests = [

        (["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], False),
        (["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True),


        (["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "12 + 34", "56 - 78"], False),


        (["32 * 8", "1 - 3801"], False),


        (["3a + 2", "123 - 49"], False),


        (["12345 + 49", "678 - 23"], False)
    ]

    for i, (problems, answers) in enumerate(tests, start=1):
        print(f"\nTest {i}:")
        output = arithmetic_arranger(problems, answers)
        print(output)

if __name__ == "__main__":
    run_tests()


