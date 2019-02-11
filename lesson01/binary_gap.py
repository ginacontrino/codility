def solution(num):
 biggestGap = 0
 currentGap = 0
 
 while not num&1:
   num = num >> 1

 while num > 0:
  if num&1:
   if currentGap > biggestGap:
    biggestGap = currentGap
   currentGap = 0
  else:
   currentGap += 1

  num = num >> 1  

 return biggestGap
