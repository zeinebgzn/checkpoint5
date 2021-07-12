#!/usr/bin/env python
# coding: utf-8

# In[3]:


# 1 
class Point3D(object):
    def __init__(self, x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self): # repr affiche directement l'object en chaine de caractères
        return "(%d, %d, %d)" % (self.x, self.y, self.z) # pour remplacer le %d en chaque self
        
my_point = Point3D(1,2,3)
print(my_point)


# In[4]:


# 2
class Rectangle(object):
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
        
    def perimeter(self):
        
        return 2*self.length + 2*self.width
    
    def area(self):
        
        return self.length*self.width
    
my_rectangle = Rectangle(3,4)

print("The perimeter of the rectangle is:", my_rectangle.perimeter())
print("The area of the rectangle is:", my_rectangle.area())


# In[1]:


# 3
from math import *


class Circle(object):
    def __init__(self, O, r,x,y,circle_x,circle_y):
        self.O = O
        self.r = r
        self.x = x
        self.y = y
        self.circle_x = circle_x
        self.circle_y = circle_y
    
    def perimeter(self):
        
        return 2*pi*self.r
    
    def area(self):
        
        return pi*self.r*self.r
    
    def isInside(self):
        
        if ((self.x - self.circle_x) * (self.x - self.circle_x) +
        (self.y - self.circle_y) * (self.y - self.circle_y) <= self.r * self.r):
            return True
        else:
            return False
x = 1
y = 1
circle_x = 0
circle_y = 1
rad = 2

cercle = Circle(0,rad,x,y,circle_x,circle_y)
print(cercle.perimeter())
print(cercle.area())
print(cercle.isInside())
        


# In[2]:


# 4
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
  
    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)
  
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
  
    def display(self):
        print("\n Net Available Balance=",self.balance)
  
# Driver code
   
# creating an object of class
s = Bank_Account()
   
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()


# In[ ]:




