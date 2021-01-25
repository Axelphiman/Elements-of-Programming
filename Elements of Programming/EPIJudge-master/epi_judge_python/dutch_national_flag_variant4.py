def dutch_national_flag_variant4(A):
    last_zero = 0
    found = False

    for i in reversed(range(len(A))):
        if A[i] == 0 and not found:
            last_zero = i
            found = True
        if A[i] != 0 and found:
            A[i], A[last_zero] = A[last_zero], A[i]
            last_zero -= 1


A = [0,'D',0,0,'A',0,'E','B',0,0,0,'C',0]
dutch_national_flag_variant4(A)
print(A)