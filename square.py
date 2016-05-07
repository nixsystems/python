'''
Learning Pythong 4th E
Created on May 5, 2016

@author: eddy
'''

def square(arg):
    return arg ** 2

class Sum:
    def __init__(self, val):
        self.val = val 
        
    def __call__(self, arg):
        return self.val + arg
    
class Product:
    def __init__(self, val):
        self.val = val 
        
    def method(self, arg):
        return self.val * arg 
    
class Negate:
    def __init__(self, val):
        self.val = -val
        
    def __repr__(self):
        return str(self.val)
    
def main():    
    sobject = Sum(2)
    pobject = Product(3)
    actions = [square, sobject, pobject.method, Negate] # function, instance, method, class
    
    for act in actions:
        print(act(5))
        
    print('-'* 11)
    print('List comprensions')
    print([act(6) for act in actions])
    
if __name__ == '__main__': main()



