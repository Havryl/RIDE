# Automatically generated by 'package.py' script.

VERSION = '0.29.2'
RELEASE = 'final'
TIMESTAMP = '20101110-140657'

def get_version(sep=' '):
    if RELEASE == 'final':
        return VERSION
    return VERSION + sep + RELEASE

if __name__ == '__main__':
    import sys
    print get_version(*sys.argv[1:])
