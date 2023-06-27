import sys, traceback

def safe(func, *pargs, **kargs):
    try:
        func(*pargs, **kargs)
    except:
        traceback.print_exc()
        print('Got %s %s' % (sys.exc_info()[0], sys.exc_info()[1]))

if __name__ == '__main__':
    import exercise2
    safe(exercise2.oops)