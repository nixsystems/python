'''
Learning Python 4thE
Created on May 5, 2016

@author: eddy
'''

class Selfless:
    def __init__(self, data):
        self.data = data
        
    def selfless(arg1, arg2): # No instance missing (self) simple function
        return arg1 + arg2
    
    def normal(self, arg1, arg2): # Passing instance (self) Bond method
        return self.data + arg1 + arg2

x = Selfless(2)
print(x.normal(2, 5))

z = Selfless.selfless(3, 4)
print(z)
