''' Implement question number 2, 3, 4 and 5 from Session 1 Exercise as different functions in a single file. '''

#Exercise 2. Write a program that will convert Fahrenheit to Celsius in degrees.

F = float(input("Enter the temperature in Fahrenheit "))

def temp(F):
    C = (F - 32) * (5/9)
    print("The temperature in Celsius is:",C) 

temp(F)

#Exercise 3. Write a program that takes seconds as time units and converts it to minutes and seconds. 

seconds = int(input("Enter time in seconds "))

def time_converter(seconds):
    min = seconds//60
    sec = seconds%60
    print(min,"minutes",sec,"seconds")

time_converter(seconds)

#Exercise 4. Consider a list of any arbitrary elements. Your code should print the length of the list and first and fourth element of the list.

list = ['nepal','hetauda','kathmandu','chitwan','europe']

def test(list):
    print(list)
    a = len(list[0])
    print("Length of the first element is",a)
    b = len(list[3])
    print("Length of the fourth element is", b)
    print(b)

test(list)

#Exercise 5. Create a list of any arbitrary elements. Your code should show the list methods as pop, insert and remove.

list1 = ['nepal','hetauda','kathmandu','chitwan','europe']
def test1(list1):
    print(list1)
    list1.pop(1)
    print(list1)
    list1.insert(1,'Lalitpur')
    print(list1)
    list1.remove('europe')
    print(list1)

test1(list1)

