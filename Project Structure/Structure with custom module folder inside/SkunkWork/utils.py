"""SkunkWork Utils"""
import datetime


def clog(*args):
    msg = '>>> '+str(datetime.datetime.now()).split('.')[0] + ' :'
    for s in args:
        msg = msg + ' ' + str(s)
    print(msg)
    print('***')
    print('###')


def main():
    clog('Hello World!')


    # run
if __name__ == '__main__':
    main()
