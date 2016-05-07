'''
Learning Python 4th E
Created on May 5, 2016

@author: eddy
'''
from lister import ListInherited

class Spam(ListInherited):   # Inherit a __str__ method
    def __init__(self):      # No __repr__ or __str__
        self.data1 = "food"
        

def main():
    x = Spam()
    print(x)
    
if __name__ == '__main__': main()

