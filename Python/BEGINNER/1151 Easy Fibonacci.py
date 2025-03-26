position = int(input())
previous_term = 0
current_term = 1
for term in range(position):
    if term == 0:
        print(previous_term, end=' ')
    elif term == 1:
        print(current_term, end=' ')
    elif term < (position - 1):
        result_term = previous_term + current_term
        previous_term = current_term
        current_term = result_term
        print(result_term, end=' ')
    else:
        result_term = previous_term + current_term
        previous_term = current_term
        current_term = result_term
        print(result_term)
