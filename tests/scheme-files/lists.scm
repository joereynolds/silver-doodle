#lang racket

(define (len l)
  (if (null? l)
      0
      (+ 1 (len (cdr l)))
  )
)


(define (app l1 l2)
  (if (null? l1)
      l2
      (cons (car l1) (app (cdr l1) l2))
  )
)

(define hw (list "A" "B" "C"))
(define hw2 (list "Bambuk" "Hasfalt"))
(define nums (list 5 9 354 0 -12))