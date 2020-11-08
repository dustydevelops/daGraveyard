

import time
from random import randint, seed




def message():
  try:
   seed(1)
   for _ in range(10):
     x = randint(0,10)
   if x <= 1:
     print('equal to or less than 1',x)
   elif x > 1:
     print('greater than 1',x)
  except:
    print('fuck')
message()


def somethinWrong():
 try:
  a = 1/0

 except Exception as e:
  print(e)
somethinWrong()
