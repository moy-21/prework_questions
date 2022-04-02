# Question 1 :  Write function hello user name 
def hello_name(user_name):
    user_name = input("Username: ")
    print("Hello " + user_name + "!")
    
hello_name('Username')
    

# Question 2 : Write pyhton function, first_odds that prints the odd numbers from 1-100
# and returns nothing  
def first_odds():
    first_odds = list(range(1,101,2))
    print(first_odds)
    return first_odds
first_odds()


# Question 3 : Write a pyhton function max_num_in_list to return the max number given list.
def max_num_in_list(a_list):
    a_list = [1,5,10,20,13,101]
    print(max(a_list))
    return a_list
max_num_in_list(int)


# Question 4 : Write a function to return if the given year is a leap year. 
def is_leap_year(a_year):
    a_year = int(input("What is the year? : "))
    if a_year % 4 == 0 :
        print("it is a leap year!")
    elif a_year % 400 == 0:
         print("it is a leap year!")
    else:
        print("It is not")
    return a_year
is_leap_year(a_year= int)


# Question 5 : Write a function to check to see if all numbers in the list are consecutive numbers.
def is_consecutive(a_list2):
    a_list2 = [2,3,4,5,6,7,8]
    if a_list2 == sorted(a_list2):
        print("they are consecutve")
    else:
        print("Its not sorted")

    return a_list2


is_consecutive(str)