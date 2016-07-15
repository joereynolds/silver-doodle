import argparse

import lint

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file')

    args = parser.parse_args()

    if args.file:
        print(lint.show_errors(args.file))


if __name__ == '__main__':
    run()
