(defun cubesum (x)
  (if (null x) 
      0
      (+ (expt (car x) 3) (cubesum (cdr x)))
  )
)

(defun iscube (x)
  (if (= 0  (mod x (expt x (/ 1 3)))) 
      T
      nil
  )
)

(defun nocubes (x)
  (if (null x)
      nil
      (if (iscube (car x))
	  (nocubes (cdr x))
	  (cons (car x) (nocubes (cdr x)))
      )
  )
)
