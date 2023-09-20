#print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("__file__"), '.')))
#print(sys.path)

import example_module

if __name__ == "__main__":
    #print("__main__ in test_main.py")
    example_module.print_it("Called from test_main.py")
