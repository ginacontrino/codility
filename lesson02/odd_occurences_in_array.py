
from functools import reduce

def solution(array):
	return reduce((lambda x, y: x^y), array)

print(solution([9,3,9,3,9,7,9]))
