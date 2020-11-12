'''Implement question number 1, 2 and 4 from Session 2 Exercise as different functions in a single (.py) file.'''

'''1. Choose a list of your choice and find the sum of all elements of that list. For example, the
sum of [6,9,7,5,4] is 31.'''

example = [6,9,7,5,4]

def ele(choice):
    sum = 0
    for str1 in choice:
        sum += str1
    print("The sum of the list is:",sum)

ele(example)



'''2. Write a program that returns a list which contains common elements from two lists. Avoid
the duplicate elements from lists.'''

a = [1, 1, 3, 5, 7, 9, 9]
b = [2, 1, 6 ,9, 2, 1, 3, 5]
def dup(a,b):
    inter = list(set(a) & set(b))
    print('The common element from the list are',inter)

dup(a,b)

'''4. Write a code to ask an input from the user which is a string and display the string along
with its length.'''

inp = str(input("Enter a string to check the length "))
def length(e):
    cou = 0
    print("The string is:",e)
    for each in e:
        cou += 1
    print("The length of the string is:",cou)

length(inp)
