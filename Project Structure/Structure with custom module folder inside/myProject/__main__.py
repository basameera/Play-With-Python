
# import sys
# sys.path.append(r'C:\Users\Sameera\Documents\Github\Play-With-Python\Project Structure\Structure with custom module folder inside')

from SkunkWork import skunkwork as sw
from SkunkWork.utils import clog

if __name__ == "__main__":
    print('main')
    swt = sw.nnTrainer()
    swt.compile()

    swd = sw.dSet()
    swd.compile()

    clog('hello from myProject')