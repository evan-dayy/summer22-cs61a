(define (tail-replicate x n)
  (define (tail-replicate-tail x n result)
    (if (= n 0)
      result
      (tail-replicate-tail x (- n 1) (cons x result))
    )
  )
  (tail-replicate-tail x n ())
)