from functools import reduce

def solution(array):
 completeArray = list(range(1, len(array)+2))
 return reduce((lambda x, y: x^y), array + completeArray)

print(solution([2,3,5,1]))
