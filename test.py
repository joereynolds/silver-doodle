import unittest

import lint
import messages


class TestLinter(unittest.TestCase):

    def test_it_finds_the_errors(self):
        errors = lint.get_errors('test-file.ss')

        self.assertIn(messages.message['tabs'], errors[0])
        self.assertIn(messages.message['lonely_parenthesis'], errors[1])
        self.assertIn(messages.message['lonely_parenthesis'], errors[2])
        self.assertIn(messages.message['line_limit'], errors[3])
        #self.assertIn(messages.message['blank_space'], errors[4])

    def test_it_reports_the_correct_line_number(self):
        errors = lint.get_errors('test-file.ss')

        line_number = 1
        self.assertEqual(errors[0][line_number], 0)
        self.assertEqual(errors[1][line_number], 7)
        self.assertEqual(errors[2][line_number], 8)

    def test_it_gets_the_content_for_a_given_line(self):
        content = lint.get_content_for_line(8, 'test-file.ss')
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
            lint.show_errors('test-file.ss')
            output = out.getvalue().strip()
            self.assertIn('Tabs are not needed', output) 
        finally:
            sys.stdout = saved_stdout


if __name__ == '__main__':
    unittest.main()
