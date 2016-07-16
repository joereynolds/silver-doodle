### Todo
- Are there off-by-one errors in the report?
    - Not sure if line numbers should start at 0 or 1, probably 1.
- The tests on the test file are brittle
    - Everytime a new lint rule is introduced, it breaks the tests.
      Just test the actual string instead of the file
