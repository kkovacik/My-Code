;Kevin Kovacik

; this function determines if y is apart of list x, returns nil otherwise. 

(defun xmember (x y)
  (if (equal (car x) y)
      (atom y)
      (if (null(cdr x))
	  nil
	  (xmember (cdr x) y)
      )
  )
)

;this function turns a multidimensional list into a single dimensional list returns nil if list is empty

(defun flatten (x)
  (if (null x)
      nil
      (if (atom (car x))
	  (cons (car x) (flatten (cdr x)))
          (flatten (cons (caar x) (cdr x)))
      )
  )
)

; Starting with the first element in the second list, this function generates a list alternating with elements from each list. 
; If one list is longer it simply adds the remaining elements 

(Defun mix (L1 L2)                     
  (if (null L2)
      (if (null L1)
	  nil
	  (cons (car L1) (mix L2 (cdr L1)))
      )
      (cons (car L2) (mix (cdr L2) L1))
  )
)

;This function is the opposite of mix, starting with the first element it creates two lists, one with odd indexed objects, one with even indexed objects

(Defun split (L)
  (if (null L)
      (list (list nil) (list nil))
      (cons (odds L) (list (evens L)))    
  )
)

(Defun odds (L)
  (if (null L)
      nil
      (cons (car L) (odds (cddr L)))
  )
)

(Defun evens(L)
  (if (null (cdr L))
      nil
      (cons (cadr L) (evens (cddr L)))
  )
)

;This function determines the what numbers in Lsum to get 'x', returns nil otherwise
(defun subsetsum (x L)
  (if (< (sum_list L) x)
      nil
      (check_sum x (sort (copy-list (check_list x L)) #'>)) 
  )
)

;these are the helper functions
(defun check_sum(x L2)
  (if (= x 0)
      nil
      (if (or (null L2) (< x 0) (< (sum_list L2) x))
	  nil
	  (if (<= (car L2) x)
	      (cons (car L2) (check_sum (- x (car L2)) (cdr L2)))
	      (check_sum x (cdr L2))
	  )
      )
  )
)

(defun sum_list (L)
  (if (null L)
      0
      (+ (car L) (sum_list (cdr L)))
  )
)   

(defun check_list (x L) 
  (if (null L)
      nil
      (if (< x (car L))
		(check_list x (cdr L))
		(cons (car L) (check_list x (cdr L)))
      )
  )
)
