import config
import messages


def get_errors(_file):

    errors = []

    with open(_file) as file_to_lint:
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

            if it_has_a_brace_error(line_content):
                errors.append([
                    messages.message['lonely_parenthesis'],
                    line_number
                ])

    return errors

def it_has_a_brace_error(line_content):
    line_content = line_content.strip()
    return (
        len(line_content) == 1 and (
            '(' in line_content or 
            ')' in line_content
        )
    )

def get_content_for_line(line_number, _file):
    with open(_file) as file_to_read:
        for line_num, line_content in enumerate(file_to_read):
            if line_num == line_number:
                return line_content

def show_errors(_file):
    errors = get_errors(_file)
    for error_message, line_number in errors:
        print(error_message, line_number)
