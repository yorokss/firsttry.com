"""
created by: yogesh rajput
on 27/09/2022
Level – 1
1. Take a list of 10 numbers from the users.
a. Remove all the even numbers from the list.
b. Create a list from the above list which contains only even numbers.
c. Create the list from the above list which contains only odd numbers.
d. Split the list into 2 lists, so that list-1 contains all the numbers which are less than 50,
and the list-2 contains all the numbers greater than and equal to 50.
"""



list=[]
number=[]
even=[]
odd=[]
more_50=[]
less_50=[]
for i in range(5):
    list = int(input("Enter number here "))
    number.append(list)
print(number)
only_odd = [num for num in number if num % 2 == 1]
only_even = [num for num in number if num % 2 == 0]
print(only_odd)
print(only_even)

if i in number <= 50:
    number.append(more_50)

    print(more_50)
else:
    number.append(less_50)
    print(less_50)



"""if number % 2==0:
    number.append(even)
else:
    number.append(odd)
print(even)
print(odd)
print(number)"""

