import math

def cube (num):
	return(num*num*num)
print(cube(3))
print(cube(-5))

def oddEvenOther (num1):
	if num1 == 0:
		return ('neither')
	if num1%2 == 0:
		return ('even')
	if num1%2 == 1:
		return ('odd')
print(oddEvenOther(2))
print(oddEvenOther(3))
print(oddEvenOther(0))

def diff17 (num2):
	if num2 <= 17:
		return(abs(17-num2))
	else:
		return(abs(17-num2)*2)
print(diff17(14))
print(diff17(22))

def sumOrThreeX (num3, num4, num5):
	if num3 == num4 & num4 == num5:
		return (num3*9)
	else:	
		return (num3+num4+num5)
print(sumOrThreeX (2, 2, 2))
print(sumOrThreeX (3, 4, 5))


def sumOrZero (num6, num7, num8):
	if num6==num7 or num7==num8 or num6==num8:
		return(0)
	else:
		return(num6 + num7 + num8)
print(sumOrZero(2, 2, 1))
print(sumOrZero(3, 2, 3))
print(sumOrZero(3, 3, 3))
print(sumOrZero(3, 2, 1))

def countRepeat (num9):
	i = 0
	while i < num9:
		print(i)
		print(i)
		i += 1
	return num9
print(countRepeat(5))

sevenNum = 1/7
numString = sevenNum-math.floor(sevenNum)

for i in range (5):
  tempNum = numString * 10
  num = math.floor(tempNum)
  print (num)
  numString = tempNum - num
def roll_dice(num, list):
  total = 0
  for i in range(num):
    num = list[i]
    if num == 1:
      return 1
    total = total + num
  return total

  
  