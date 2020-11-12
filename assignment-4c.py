'''Implement question number 1, 2 and 6 from Session 3 Exercise as different functions in a single(.py) file'''

'''1. Write a program to display all prime numbers from 1 to 100'''

def prime():
    print("Prime numbers are: ")
    for i in range(1,101):
        c = 0
        for j in range(1,101):
            if i % j == 0:
                c += 1
        if c == 2:
            print(i)

prime()

'''2. Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)'''

string1 = str(input("Enter a string to check for the palindrome "))

def pal(string1):
    pal = string1[::-1]
    if pal == string1:
        print(string1 + ' is palindrome')
    else:
        print(string1 + ' isn\'t paldinrome')

pal(string1)

'''6. Create a dictionary that has a key value pair of letters and the number of occurrences of
that letter in a string.
Given a string “pineapple”. The result should be as:
{“p”:3, “i”:1, “n”:1, “e”:2, “a”:1, “l”:1}
Don’t worry about the order of occurrence of letters'''


string6 = "pineapple"
string6 = string6.lower()

def test(string6):
    dic1 = {}
    for i in string6:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1
            
    print("The required dictionary is:",dic1)

test(string6)


   