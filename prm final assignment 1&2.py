#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python - Question 01
# You will be given a list. You have to print a list whose 1st element should be largest 
# and 2nd should be the smallest then the 3rd should be 2nd largest and 4th should be 2nd smallest and so on.
# Input Format:
# The first line will have space-separated elements of the list.
# Output Format:
# Print the required list.
# Sample Input 0:
# 1 2 3 4 5 6
# Sample Output 0:
# 6 1 5 2 4 3

s_list= [int(x)for x in input("Enter elements of list separated by space: ").split()]
if len(s_list)%2 == 0:
    max_val= []
    for i in range(len(s_list)//2):
        max_val.append(max(s_list))
        given_list.remove(max(s_list))
        given_list= sorted(s_list)
    for k,v in zip(max_val,s_list):
        print(k,v, end= ' ')
else:
    print("Enter even number of elements")


# In[ ]:


# Python - Question 02
# Find nth fibonacci number. If it starts with 0,1,1,2.....
# Also, Print Incorrect Input if n is less than or equal to 0.
# Input Format:
# Call the function with n
# Output Format:
# Print the nth fibonacci number
# Sample Input 0:
# 4
# Sample Output 0:
# 2
# Sample Input 1:
# 0
# Sample Output 1:
# Incorrect input

def fibonacci(n):
    if n > 0:
        f_series= []
        a= 0
        b= 1
        c=a+b
        for i in range(n):
            f_series.append(a)
            a=b
            b=c
            c=a+b
        return f_series[-1]
    else:
        return "Incorrect input"

number= int(input("Enter the nth term you want: "))
fibonacci(number)


# In[ ]:




