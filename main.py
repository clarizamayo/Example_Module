import os
import sys
import add
from library.multiply import multiply
        
if __name__ == '__main__':
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    print(add.add(x,y))
    print(multiply(x,y))