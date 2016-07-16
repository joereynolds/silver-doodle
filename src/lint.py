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

                if '\t' in line_content:
                    errors.append([
                        messages.message['tabs'], 
                        line_number
                    ])

                if len(line_content) > config.line_limit:
                    errors.append([
                        messages.message['line_limit'],
                        line_number
                    ])

                if self.it_has_a_brace_error(line_content):
                    errors.append([
                        messages.message['lonely_parenthesis'],
                        line_number
                    ])

                if self.it_has_no_blank_line_between_procedures(
                    line_number,
                    line_content
                ):
                    errors.append([
                        messages.message['blank_line'],
                        line_number
                    ])
                if self.it_has_a_badly_named_variable(
                    line_content
                ):
                    errors.append([
                        messages.message['bad_variable'],
                        line_number
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

    def it_has_no_blank_line_between_procedures(self, line_number, line_content):
        if '(define' in self.get_content_for_line(line_number).strip():
            if not self.get_content_for_line(line_number -1).startswith(';') and self.get_content_for_line(line_number -1) != '\n':
               return True

    def it_has_a_badly_named_variable(self, line_content):
        #Matches camelCase
        if re.match('.*(define|let)\s*[a-z]*[A-Z]', line_content):
            return True
        #Matches snake_case
        if re.match('.*(define|let)\s*[a-z]*_', line_content):
            return True

    def get_content_for_line(self, line_number):
        return self.file_content[line_number][1]

    def show_errors(self):
        errors = self.get_errors()
        for error_message, line_number in errors:
            print(error_message, line_number)
