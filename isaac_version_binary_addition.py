# Code Wars Binary Addition
# Isaac's version

import math

def add_binary(a,b):
	# Don't use the variable name 'sum'
    sum = a+b
	# This adds an error message
    assert sum > 0, "Sum needs to be greater than zero"
    full_num = []
	# This allows range to be only as big as the number in question
    for i in range(int(math.log(sum, 2)), -1, -1):
        place = 2**i
        value = '0'
        if sum >= place:
            value = '1'
            sum = sum - place
        full_num.append(value)
    result = ''.join(full_num)
    return result

# test of sum of 0
#print(add_binary(0, 0))
