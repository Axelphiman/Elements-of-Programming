def given_sum_subarray(sum, A):
    last_element = 0
    till_sum = 0
    first_element = 0
    for i in range(len(A)):
        till_sum += A[i]
        if till_sum > sum:
            till_sum -= A[first_element]
            first_element += 1
        last_element += 1
        if till_sum == sum:
            return A[first_element:last_element]
    return 0
print(given_sum_subarray(15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
