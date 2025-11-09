#Q 1>#import math
# print(math.ceil(65.65))
# print(math.ceil(65.47))
# print(math.fabs(-67.58))
# print(math.fabs(3))
# print(math.exp(2.7))
# print(math.log(45,2))
# print(math.log10(1000))
# print(math.pow(4,1/2))
# print(math.sqrt(121))
# print(math.radians(30))
# print(math.degrees(math.pi/2))

# Q 3> print(chr(72))
# print(complex('1+2j'))
# print(divmod(5,2))
# print(max('a','b','AB'))

# Q 4> def star():
#   print('     *')
#   print('  *  *  *')
#   print('* *  *  *  *')
#   print('  *  *  *')
#   print('     *')

# star()
# def dollar():
#   print('$ $ $ $ $')
#   print('$       $')
#   print('$       $')
#   print('$       $')
#   print('$ $ $ $ $')

# dollar()  

# Q 5> def nMultiple(a=0,num=1):
#   return a * num
# print(nMultiple(5))
# print(nMultiple(5,6))
# print(nMultiple(num=7))
# print(nMultiple(num=6,a=5))
# print(nMultiple(5,num=6))

# Q 6>
# def test(a,b):
#     a=a+b
#     b=a-b
#     a=a-b
#     print('a=',a)
#     print('b=',b)
# test(5,8) 
# def func():
#     pass
# a=func()
# print(a) 

# Q 7>
# import math
# def areaTriangle(side1,side2,side3):
#     s=(side1+side2+side3)/2
#     area=pow(s*(s-side1)*(s-side2)*(s-side3),1/2)
#     return area
# def main():
#     s1=float(input('enter 1st side of the triangle :'))
#     s2=float(input('enter 2nd side of the triangle :'))
#     s3=float(input('enter 3rd side of the triangle :'))
#     assert s1+s2>s3 and s1+s3>s2 and s2+s3>s1
#     print('The area of triangle is :',areaTriangle(s1,s2,s3))

# main()    
