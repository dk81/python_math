# Arithmetic Sequence & Series Functions


# Formula: 
    
# Arithmetic Sequence Formula: end = start + (n - 1)d
# end - start = (n - 1)d
# (end - start) / d = n - 1
# (end - start) / d + 1 = n 

def find_term_n(start, n, diff):
    if start % 1 != 0:
        print("Please choose an integer.")
    elif n % 1 != 0 and n < 1:
        print("Please choose a positive whole number.")
    else:
        term_n = start + (n - 1)*diff
        return term_n
    
print(find_term_n(start = 1, n = 10, diff = 6))


def find_numTerms_arithSeq(start, end, diff):
    if start % 1 != 0:
        print("Please choose an integer.")
    numTerms = 1 + (end - start) / diff
    if numTerms > 0:
        return int(numTerms)
    else:
        print("The number of terms cannot be negative. Try again.")


print(find_numTerms_arithSeq(1, 10, -1))


# Arithmetic Series formula:
# Finding the sum of an arithmetic series.
# Reference: https://stackoverflow.com/questions/21583758/how-to-check-if-a-float-value-is-a-whole-number



def find_arithmetic_seriesSum_verOne(start, end, n):
    if start % 1 == 0 and start > 0:
        if end % 1 == 0 and end > 0 and end > start:
            total = 0.5*n*(start + end)
            return total
    else:
        print("Choose a starting number that is a whole positive number please.")
        
print(find_arithmetic_seriesSum_verOne(start = 1, end = 10, n = find_numTerms_arithSeq(1, 10, 1)))
