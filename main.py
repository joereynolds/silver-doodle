import argparse

import lint

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')

    args = parser.parse_args()


    if args.file:
        linter = lint.Linter(args.file)
        print(linter.show_errors())


if __name__ == '__main__':
    run()
