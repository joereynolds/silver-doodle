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
You have trailing whitespace 34
```

## Using it

```
cd silver-doodle/src
python3 silver-doodle.py YOUR_FILE.ss
```

## Tests

To run the unit tests, make sure you're in the `src` directory and run
`python3 test.py`

All tests should pass.

### Acceptance tests

There are acceptance tests though it's not 100% necessary to run these as the unit tests will cover most cases. If you do want to try them, you'll need
[shelltest](https://github.com/liquidz/shelltest#getting-started).

Once you have that installed, it's just a case of doing

`shelltest filename.py`


## Helping Out

I definitely need help, so yeah contribute!

To do

- silver-doodle needs to be bundled into a single executable
- 'Sassy' errors need doing
- More difficult rules such as indentation still need to be programmed in
- More tests
- Integration with Syntastic
    - I have no idea what's involved with this but I think it needs
      to be packaged before this is possible
