
def solution(array, rotations):
 arrayLength = len(array)

 if arrayLength == 0:
 	return []

 rotations = (rotations + arrayLength) % arrayLength
 if rotations == 0 or arrayLength == 0 or arrayLength == rotations:
  return array

 newArray = []
 for i in range(arrayLength):
  newPosition = (i + rotations) % arrayLength
  newArray.insert(newPosition, array[i])
 
 return newArray	
   
print(solution([3, 8, 9, 7, 6] , 3))
