#question 1

# f=['prabh','anmol','simran','arsh','deep']

# f.append('priyanshu')#add name on last
# print(f)
# f.insert(2,'jassi')#index ,value

# print(f)


# #question 2

# l=[]
# for i in range(10):
#     val=int(input("Enter value"))
#     l.append(val)
# print(l)


#question 3

# l1= [1,10,100,3,6,8] 
# l1.insert(2,53)
# l1.append(5)
# print(l1)
# print(len( l1))


# # Find all of the words in a list of strings that are less than 4 letters
# l2=['hii','how','are','you','jassi','arshdeep','priyanshu']
# l5=[]
# for i in l2:
#     if len(i)<4:
#         l5.append(i)

# print(l5)


# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even, 
# and the word ‘odd’ if the number is odd. Result would look like ‘odd’,'even',........ 

# l1=[]
# for i in range(20):
#     x=int(input("Enter number "))
#     l1.append(x)
# print(l1)
# l2=[]
# for i in l1:
#     if i%2==0:
#         l2.append('even')
#     else:
#         l2.append('odd')

# print(l2)




# l=[]
# for i in range(1000):
#     if i%7==0:
#         l.append(i)
# print(l)

# x=str(input("Enter string: "))
# print(x)
# space=x.count(' ')
# print(space)

# l1=['hello friend','How are you','hjvb hfdsfhb hbhds']
# l1=[ i.count(' ') for i in l1 if " " in l1]
# print(l1)
# print(sum(l1))



# l= [i for i in range(1000) if i%7==0]
# print(l)



# l=[int(input("Enter {0}".format(i+1))) for i in range(10) ]