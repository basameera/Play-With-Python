# imports
from __future__ import print_function
from txt_logger import logger

# define the function blocks
def test_logger():
    log = logger()
    log.printHeader()
    log.write('something')
    log.write('more things')

def sqr():
    print("n is a perfect square\n")


# map the inputs to the function blocks
options = {0 : test_logger,
           1 : sqr,
           
}

if __name__ == '__main__':

    test_number = 0
    options[test_number]()