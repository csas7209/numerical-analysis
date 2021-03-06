;; The Secant Method
;; Section 1.2, p. 38 of Applied Numerical Analysis

;; secant takes as input a function f and 2 initial values (x0 and x1),
;; from which a third value is computed.
;; The function then calls itself recursively with newly computed values,
;; until a root of f is found.

(load "helpers")
(define (secant f x0 x1)
  (define x2 (linear-interpolate f x0 x1))

  (println x0 " " x1 " " x2 " " (f x2))
  (if (close-enough-to-zero? (f x2))
      x2
      (secant f x1 x2)))

(println (secant example-f 1 0))
