'''
Learning PYthon 4th E
Created on May 5, 2016

@author: eddy
'''

class Number:
    def __init__(self, base):
        self.base = base
    
    def double(self):
        return self.base * 2
    
    def triple(self):
        return self.base * 3
    
def main():
    x = Number(2)
    y = Number(3)
    z = Number(4)
    x.double()
    
    acts = [x.double(), y.double(), y.triple(), z.double()]
    for act in acts:
        print(act)
        
if __name__ == '__main__': main()
    
