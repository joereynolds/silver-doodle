#lang racket

; A function that calculates windchill
; parameters: t - temperature, v - velocity
(define (windchill t v)
  (+ 35.74
     (* 0.6215 t)
     (* (expt v 0.16)
        (- (* 0.4275 t) 35.75)
     )
  )
)