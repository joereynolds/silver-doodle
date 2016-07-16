# silver-doodle

A linter for the Scheme programming language

## Getting it

`git clone https://github.com/joereynolds/silver-doodle`

## Example

`python3 silver-doodle.py tests/scheme-files/test-file.ss`

Outputs

```
Tabs are not needed 0
Parenthesis should never be on their own line 7
Parenthesis should never be on their own line 8
Badly named variable. Variables should be dash-separated 11
Badly named variable. Variables should be dash-separated 15
This line is above the recommended line limit of 100 columns 20
There should be a blank line between each procedure definiton 28
There should be a blank line between each procedure definiton 31
```

## Using it

```
cd silver-doodle/src
python3 silver-doodle.py YOUR_FILE.ss
```

## Tests

To run the tests, make sure you're in the `src` directory and run
`python3 test.py`

All tests should pass.

## Helping Out

I definitely need help, so yeah contribute!

To do

- silver-doodle needs to be bundled into a single executable
- 'Sassy' errors need doing
- More difficult rules such as indentation still need to be programmed in
- More tests
