'''
Learning Python 4th E
Created on May 6, 2016

@author: eddy
'''

class ListTree:
    def __str__(self):
        self.__visited = {}
        return '<Instance of {}, address {}:\n{}{}>'.format(self.__class__.__name__,
                                                            id(self),
                                                            self.__attrnames(self, 0),
                                                            self.__listclass(self.__class__, 4))
    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{}<Class {}, address {}: (see above)>\n'.format(dots,
                                                                      aClass.__name__,
                                                                      id(aClass))
        else:
            self.__visited[aClass] = True
            genabove = (self.__listclass(c, indent+4) for c in aClass.__bases__)
            return '\n{}<Class {}, address {}:\n{}{}{}>\n'.format(dots,
                                                                 aClass.__name__,
                                                                 id(aClass),
                                                                 self.__attrnames(aClass, indent),
                                                                 ''.join(genabove),
                                                                 dots)
    def __attrnames(self, obj, indent):
        space = ' ' * (indent + 4)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += space + '{}=<>\n'.format(attr)
            else:
                result += space + '{}={}\n'.format(attr, getattr(obj, attr))
        return result
    
def main(): pass

if __name__ == '__main__': main()
