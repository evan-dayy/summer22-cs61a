(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (enumerate-count s cnt)
    (if (null? s) 
      nil
      (cons 
        (list cnt (car s))
        (enumerate-count (cdr s) (+ 1 cnt))
      )
    )
  )
  (enumerate-count s 0)
)
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2)
  ; BEGIN PROBLEM 16
  (cond 
    ((null? list1) list2)
    ((null? list2) list1)
    ((ordered? 
      (car list1)
      (car list2))
      (cons (car list1) (merge ordered? (cdr list1) list2))
    )
    (else
    (cons (car list2) (merge ordered? list1 (cdr list2))))
  
  )
  
)
  ; END PROBLEM 16

