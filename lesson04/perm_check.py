def solution(array):
 seen = set()
 for item in array:
  if (item > len(array)) or item < 1 or item in seen:
   return 0
  seen.add(item)	
 return 1


print(solution([5,2,1,2]))

