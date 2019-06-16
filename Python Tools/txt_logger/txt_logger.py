"""
Text file logger

To Do:
1. Add levels such as [INFO, DANGER, ...]
"""
from __future__ import print_function

class logger():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    def __init__(self, file=__file__, filename="logger.txt"):
        self.filename = filename
        self.file = file
        header = self.getHeader()
        self.write("")
        for line in header:
            self.write(line)
        self.write("")
        
    def write(self, str):
        file = open(self.filename,"a")
        file.write(str + "\n")
        file.close()

    def getHeader(self):
        import datetime as dt
        import socket
        import os
        fname = " " + os.path.basename(self.file) + " "
        tm_str = str(dt.datetime.now()).split(".")
        dtm = "> " + str(socket.gethostname()) + " | " + tm_str[0] + " <"

        len_diff = len(dtm) - len(fname)
        len_diff_half = int(len_diff/2)

        str_first, str_second = "", ""

        for _ in range(len_diff_half):
            str_first += "="
            str_second += "="
        
        if len_diff%2==1: # len_diff is a even number
            str_second += "="

        line_1 = str_first + fname + str_second
        line_3 = ""

        for _ in range(len(dtm)):
            line_3 += "="
        
        output = [line_1, dtm, line_3]
        return output

    def printHeader(self):
        headers = self.getHeader()
        for line in headers:
            print(line)


if __name__ == '__main__':

    log = logger()
    log.printHeader()
    log.write('something')
    log.write('more things')
    
