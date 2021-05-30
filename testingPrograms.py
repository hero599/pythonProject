import cmath

print('Hello Harpreet')
num1: float = 1.5
num2: float = 2.0
sumNum: float = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sumNum))

num1 = input('Enter num1: ')
num2 = input('Enter num2: ')
sumNum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sumNum))

print('The sum is %.1f' % (float(input('Enter first number: ')) + float(input('Enter second number: '))))

num1 = input('Enter no. to get sqr_root: ')
num_sqrt = cmath.sqrt(float(num1))
print('The square root of {0} is {1}'.format(num1, num_sqrt.real))
