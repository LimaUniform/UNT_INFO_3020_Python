#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Display initial message
print("Welcome to INFO 3020 Assignment 2 Compound Interest calculator. Where P’ = P(1+r/n)^nt")

#Taking input from user

#Principle amount
p = float(input("Priciple (P): $ "))

#Rate of interest
r = float(input("Interest Rate (R) E.G., '.03' for 3% interest: "))

#Number of compounding periods per year
c = int(input("Compounding Periods per Year: "))

#Number of years
t = int(input("Time (T in Years): "))

# convert rate
#r = r / 100

#Calculating compound interest
ci =  p * (pow((1 + r / c), t)) 

#Amount of interest earned
ie = ci - p

# printing the values
print("Orginal principal (P)                                 : $" , format(p, ',.2f'))
print("Amount of interest earned (P’- P)                     : $" , format(ie, ',.2f'))
print("Total value of the account at the end of the term (P’): $" , format(ci, ',.2f'))


# In[ ]:





# In[ ]:




