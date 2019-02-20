import math

def solution(initalPosition, goalPosition, jumpDistance):
 if initalPosition == goalPosition or jumpDistance == 0:
 	return 0

 return math.ceil((goalPosition - initalPosition)/float(jumpDistance))
 

print(solution(3, 999111321, 7))

