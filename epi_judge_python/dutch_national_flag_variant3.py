def dutch_national_flag_variant3(A):
    zeros = 0
    ones = len(A) - 1

    while zeros < ones:
        if A[zeros] == 1:
            A[zeros], A[ones] = A[ones], A[zeros]
            ones -= 1
        else:
            zeros += 1

    return A
A = [0,1,1,1,0,0,1,0,1,0,1,1]
print(dutch_national_flag_variant3(A))