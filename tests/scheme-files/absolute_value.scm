#lang racket

(define (abs x)
  (if (< x 0)
      (- x)
      x
   )
)

; An integer power function
; precondition: 
;   x must be a number
;   y non-negative integer
(define (int-pow x y)
  (if (<= y 0)
      1
      (* x (int-pow x (- y 1)))
  )
)

; Computations are not delayed; less overhead
(define (int-pow-iter x y acc)
  (if (= y 0)
      acc
      (int-pow-iter x (- y 1) (* acc x))
  )
)

(define (pow x y)
  (int-pow-iter x y 1)
)

; Sum of digits of an integer
(define (sum-of-digits x)
  (if (= x 0)
      0
      (+ (sum-of-digits (quotient x 10))
         (remainder x 10)
      )
   )
)

(int-pow 2 4)
(int-pow-iter 2 4 1)