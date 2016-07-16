import unittest

import lint
import messages


class TestLinter(unittest.TestCase):

    def setUp(self):
        self.linter = lint.Linter('tests/scheme-files/test-file.ss')

    #TODO flaky test! Depends on a file that can change
    def test_it_finds_the_errors(self):
        errors = self.linter.get_errors()

        self.assertIn(messages.message['tabs'], errors[0])
        self.assertIn(messages.message['lonely_parenthesis'], errors[1])
        self.assertIn(messages.message['lonely_parenthesis'], errors[2])
        self.assertIn(messages.message['bad_variable'], errors[3])
        self.assertIn(messages.message['bad_variable'], errors[4])
        self.assertIn(messages.message['line_limit'], errors[5])
        self.assertIn(messages.message['blank_line'], errors[6])
        self.assertIn(messages.message['blank_line'], errors[7])
        self.assertIn(messages.message['trailing_whitespace'], errors[8])

    #TODO flaky test! Depends on a file that can change
    def test_it_reports_the_correct_line_number(self):
        errors = self.linter.get_errors()

        line_number = 1
        self.assertEqual(errors[0][line_number], 0)
        self.assertEqual(errors[1][line_number], 7)
        self.assertEqual(errors[2][line_number], 8)

    def test_the_file_content_gets_populated(self):
        self.assertGreater(len(self.linter.file_content), 1)

    def test_it_gets_the_content_for_a_given_line(self):
        content = self.linter.get_content_for_line(8)
        self.assertEqual(content, ')\n')

    def test_it_finds_badly_named_variables(self):
        test_case = self.linter.it_has_a_badly_named_variable('(define absValue')
        other_test_case = self.linter.it_has_a_badly_named_variable('(define abs_value')
        caps_test_case = self.linter.it_has_a_badly_named_variable('(define ABS_VALUE')

        self.assertEqual(test_case, True)
        self.assertEqual(other_test_case, True)
        self.assertEqual(caps_test_case, True)

    def test_it_finds_trailing_whitespace(self):
        test_cases = [
            ['(define x 5) ', True],
            ['(define x 5)', False],   #No space
            [' (define x 5)', False],  #Leading space
            ['(define x 5)\n', False], #Different kind of space
        ]

        for test_case in test_cases:
            test_string = test_case[0]
            expected = test_case[1]
            actual = self.linter.it_has_trailing_whitespace(test_string)
            self.assertEqual(actual, expected)

    @unittest.skip('not implemented')
    def test_it_finds_comments(self):
        pass

    def test_it_shows_errors(self):
        """Does some weird stuff to stdout so we can test
        the printed output"""
        from io import StringIO
        import sys

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            self.linter.show_errors()
            output = out.getvalue().strip()
            self.assertIn('Tabs are not needed', output)
            self.assertIn('Badly named variable.', output)
            self.assertIn('You have trailing whitespace', output)
            self.assertIn('There should be a blank line', output)
            self.assertIn('This line is above the recommended line limit', output)
            self.assertIn('Parenthesis should never be on their own line', output)
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
