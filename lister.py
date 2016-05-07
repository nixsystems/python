'''
Learning Python 4th E
Created on May 5, 2016

@author: eddy
'''

class ListInherited:
    def __str__(self):
        return '<Instance of {} address {}\n{}>'.format(
                    self.__class__.__name__,
                    id(self),
                    self.__attrnames())
    
    def __attrnames(self):
        result = ''
        for attr in dir(self):                       # Instance dir()
            if attr[:2] == ' ' and attr[-2] == ' ':  # Skip internals
                result += '\tname {}=<>\n'.format(attr)
            else:
                result += '\tname {}={}\n'.format(attr, getattr(self, attr))
        return result
    
def main():
    pass
    
if __name__ == '__main__': main()
