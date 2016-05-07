'''
Created on Apr 30, 2016

@author: eddy
Boolean Tests: __bool__ and __len__
'''

class Truth:
    def __bool__(self):
        return True
    
    
class Ftruth:
    def __bool__(self):
        return True

x = Truth()
if x: print('yes!')

y = Ftruth()
if y: print('false!')
