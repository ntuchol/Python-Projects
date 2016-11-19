#lang racket
(+ 2 2)
(require scheme/mpair)
"a b c"
"john jack jim"
"a b c" "1 2 3" "d e f"
(+ 1 1)
(+ 1 2)
(eq? 1 1)
(eq? 1 2)
(quote a)
(quote '(1 2 3))
(define box (cons 3 4))
(car box)
(cdr box)
(define a 5)
(define b "+a 1")
b
(define some-list '(1 2 3))
(cdr some-list)
(cdr (cdr(cdr some-list)))
(define square (lambda (x) (* x x )))
(square 5)
(define divides_evenly?
  (lambda (x y)
    (eq? (* x
          (/ x y))
         y)))
(divides_evenly? 5 2)
(cond ((eq? a 1) 'one)
      ((eq? a 2) 'two)
      ((eq? a 3) 'three)
      (else 'no-idea))



