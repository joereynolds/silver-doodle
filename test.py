import unittest

import lint
import messages


class TestLinter(unittest.TestCase):

    def test_it_finds_the_errors(self):
        linter = lint.Linter('test-file.ss')
        errors = linter.get_errors()

        self.assertIn(messages.message['tabs'], errors[0])
        self.assertIn(messages.message['lonely_parenthesis'], errors[1])
        self.assertIn(messages.message['lonely_parenthesis'], errors[2])
        self.assertIn(messages.message['line_limit'], errors[3])
        self.assertIn(messages.message['blank_line'], errors[4])

    def test_it_reports_the_correct_line_number(self):
        linter = lint.Linter('test-file.ss')
        errors = linter.get_errors()

        line_number = 1
        self.assertEqual(errors[0][line_number], 0)
        self.assertEqual(errors[1][line_number], 7)
        self.assertEqual(errors[2][line_number], 8)

    def test_the_file_content_gets_populated(self):
        linter = lint.Linter('test-file.ss')
        self.assertGreater(len(linter.file_content), 1)

    def test_it_gets_the_content_for_a_given_line(self):
        linter = lint.Linter('test-file.ss')
        content = linter.get_content_for_line(8)
        self.assertEqual(content, ')\n')

    def test_it_shows_errors(self):
        """Does some weird stuff to stdout so we can test
        the printed output"""
        from io import StringIO
        import sys

        saved_stdout = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            linter = lint.Linter('test-file.ss')
            linter.show_errors()
            output = out.getvalue().strip()
            self.assertIn('Tabs are not needed', output) 
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
