#1
# a=int(input("enter a number:"))
# if a>0:
#     print(a,"is a positive number")
# else:
#     print(a,"is a negative number")    

#2
# a=int(input("enter a number:"))
# if a%2==1:
#     print(a,"is a odd number")
# if a%2==0:
#     print(a,"is a even number")    

#3
# a=int(input("enter a number a:"))
# b=int(input("enter a number b:"))
# def exp(a,b):
#     print(a**b)
# exp(a,b)

#4
# a=int(input("enter a number a:"))
# b=int(input("enter a number b:"))
# if a>b:
#     print("a is greater than b")
# else:
#     print("b is greater than a")    

# 5
# x=int(input("enter year"))
# if (x%4==0 and x%100==0):
#    print(x,"is a leap year")
# else:
#    print(x,"is not a leap year")

#6
# t=int(input("enter your mark"))
# if t<=100 and t>=90:
#     print("grade A")
# elif t<=89 and t>80:
#     print("grade B")
# elif t<=79 and t>=70:
#     print("grade C")
# elif t<=69 and t>=60:
#     print("grade D")
# else:
#      print("fail")

#7
# t=int(input("enter your age"))
# if t<16:
#     print("you can't drive")
# elif t<17 and t>16:
#     print("you can drive but not vote")
# elif t<24 and t>18:
#     print("you can drive and vote")
# elif t>24:
#     print("you can do pretty much anything")

#8
# x=int(input("enter a number:"))
# if (x%3==0 and x%5==0):
#    print("x,is fizzbuzz")
# elif (x%3==0):
#    print(x,"is fizz")
# elif (x%5==0):
#    print("x,is buzz")
   
#9
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")
