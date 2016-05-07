'''
Learning Python 4th E
Created on May 5, 2016

@author: eddy
'''
from listtree import ListTree

class Super:
    def __init__(self):
        self.data1 = 'spam'
        
    def ham(self): pass
    
class Sub(super, ListTree):
    def __init__(self):
        Super.__init__(self)
        self.data2 = 'eggs'
        self.data3 = 42
    
    def spam(self): pass
    
def main():
    x = Sub()
    print(x)
    
if __name__ == '__main__': main()

    
