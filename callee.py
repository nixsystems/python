'''
Created on Apr 30, 2016

@author: eddy
Call expression: __call__
'''

class Prod:
    def __init__(self, val):
        self.val = val
        
    def __call__(self, other):
        return self.val * other
    
x = Prod(3)
print(x(4))
