	; <- This is a tab which the linter should notice


;;;The linter should notice the parentheses on their own line
(define throws-bracket-error
  (lambda (x)
    x
  )
)

;;;The linter should notice bad variable naming
(define camelCaseVariable
  (lambda (x)
    x))

(define snake_case_variable
  (lambda (x)
    x))

;;;The linter should notice lines longer than 100 chars
(define a-really-long-procedure-name-which-will-cause-the-linter-to-fail-if-it-doesnt-the-linter-is-broken-and-that-makes-me-sad
  (lambda (x)
    x))

;;;The linter should notice code that is not separated by 1 blank line
(define a-procedure
  (lambda (x)
    x))
(define another-procedure
  (lambda (y)
    y))
(define one-more-for-good-luck
  (lambda (z)
    z))
  
;The linter should notice a bad comment
(define stuff
  (lambda (things)
    (things)))

;;The linter should notice another bad comment
(define stuff
  (lambda (things)
    (things)))
