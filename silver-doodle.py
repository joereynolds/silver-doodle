import sys

import lint

def run():

    try:
        linter = lint.Linter(sys.argv[1])
        linter.show_errors()
    except IndexError:
        print('Please specify a filename to lint')


if __name__ == '__main__':
    run()
