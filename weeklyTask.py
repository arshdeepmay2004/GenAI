# 1. Write a program that prints the numbers from 1 to 50. For multiples of three, print "Fizz" instead of the number, and 
# for the multiples of five, print "Buzz". For numbers which are multiples of both three and five, print "FizzBuzz"

# lis=[]
# for i in range(1,51):

#     if i%3==0:
#         lis.append("Fizz")
#     elif i%5==0:
#         lis.append("Buzz")
#     elif i%15==0:
#         lis.append("FizzBuzz")
#     else:
#         lis.append(i)

# print(lis)


# lis=['FizzBuzz'if i%3==0 and i%5==0  
#      else 'Fizz' if i%3==0
#      else 'Buzz' if i%5==0
#      else i  
      
#        for i in range(1,51) ]
# print(lis)


# ...................

# 2. Write a program to print all prime numbers between 1 and 100
# l=[i for i in range(1,101)  if isPrime(n)]  

# ..................

# 3. Write a program that asks the user for a score between 0 and 100 and prints the corresponding grade. The grading scheme is:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
n=int(input("Enter number"))
if n>100:
    print("Limit exceeded")
elif n>89 and n<101:
    print("A")
elif n>79 and n<90:
    print("B")
elif n>69 and n<80:
    print("C")
elif n>59 and n<70:
    print("D")
else:
    print("F")


