import re

import config
import messages


class Linter:

    def __init__(self, file_to_lint = ''):
        """
           @file_content = A 2d array of line numbers and line content
        """
        self.file_to_lint = file_to_lint
        self.file_content = self.populate_file_content()

    def populate_file_content(self):
        file_content = []

        try:
            with open(self.file_to_lint) as file_to_lint:
                for line_number, line_content in enumerate(file_to_lint):
                    file_content.append([line_number, line_content])
        except FileNotFoundError:
            return file_content

        return file_content

    def get_errors(self):

        errors = []

        with open(self.file_to_lint) as file_to_lint:
            for line_number, line_content in enumerate(file_to_lint):

                if self.it_has_tabs(line_content):
                    errors.append([
                        messages.message['tabs'],
                        line_number + 1
                    ])

                if self.it_exceeds_the_line_limit(line_content):
                    errors.append([
                        messages.message['line_limit'],
                        line_number + 1
                    ])

                if self.it_has_a_brace_error(line_content):
                    errors.append([
                        messages.message['lonely_parenthesis'],
                        line_number + 1
                    ])

                if self.it_has_no_blank_line_between_procedures(
                    line_number,
                    line_content
                ):
                    errors.append([
                        messages.message['blank_line'],
                        line_number + 1
                    ])

                if self.it_has_a_badly_named_variable(line_content):
                    errors.append([
                        messages.message['bad_variable'],
                        line_number + 1
                    ])

                if self.it_has_trailing_whitespace(line_content):
                    errors.append([
                        messages.message['trailing_whitespace'],
                        line_number + 1
                    ])

        return errors

    def it_has_a_brace_error(self, line_content):
        line_content = line_content.strip()
        return (
            len(line_content) == 1 and (
                '(' in line_content or
                ')' in line_content
            )
        )

    def it_has_comment_errors(self, line_content):
        """
        Rules for comments
          ';;;;' = 4 or more semicolons is a file comment
          ';;;' = Top-level comments, usually for procedures
          ';;' = Comments in the code indented to the same level
          ';' = Comment as an 'aside' to explain something, at the end of the line
        """
        pass

    def it_has_no_blank_line_between_procedures(self, line_number, line_content):
        if '(define' in self.get_content_for_line(line_number).strip():
            if not self.get_content_for_line(line_number -1).startswith(';') and self.get_content_for_line(line_number -1) != '\n' and line_number != 0:
               return True

    def it_has_a_badly_named_variable(self, line_content):
        if (self.it_matches_camel_case(line_content) or
            self.it_matches_snake_case(line_content) or
            self.it_matches_upper_case(line_content)):
            return True
        return False

    def it_matches_camel_case(self, line_content):
        return bool(re.match('.*(define|let|lambda)\s+.*[a-z]*[A-Z]', line_content))

    def it_matches_snake_case(self, line_content):
        return bool(re.match('.*(define|let|lambda)\s+.*[a-z]+_', line_content))

    def it_matches_upper_case(self, line_content):
        return bool(re.match('.*(define|let|lambda)\s+.*[A-Z]', line_content))

    def it_has_tabs(self, line_content):
        return '\t' in line_content

    def it_has_trailing_whitespace(self, line_content):
        return bool(re.search(' +$', line_content))

    def it_exceeds_the_line_limit(self, line_content):
        return len(line_content) > config.line_limit

    def get_content_for_line(self, line_number):
        return self.file_content[line_number][1]

    def show_errors(self):
        errors = self.get_errors()
        for error_message, line_number in errors:
            print(error_message, line_number)
