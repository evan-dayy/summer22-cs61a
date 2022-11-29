(
    define (over-or-under num1 num2) 
    (if (< num1 num2) -1 (if (= num1 num2) 0 1))
    
    )

(
    define (composed f g) 
    (lambda (x) (f(g x)))

    )

(
    define (square n) (* n n)
    )

(
    define (pow base exp)

    (cond   ((= 0 exp) 1)
            ((even? exp) (square (pow base (quotient exp 2))))
            (else (* base (pow base (- exp 1))))
          
        )
    )

(
    define (ascending? lst) 

    (cond ((null? (cdr lst))  #t  )
        
        (else (if (
        > (car lst) (car (cdr lst))
            )
        #f
        (ascending? (cdr lst))
        )))
    )

