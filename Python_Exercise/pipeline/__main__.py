"""Run a sequence of programs.

Each program (except the first) receives the standard output of the
previous program on its standard input, by default. There are several
alternate ways of passing data between the programs.

"""

import argparse

def _launch():
    print('Pipeline launched!')
    parser = argparse.ArgumentParser(prog = 'python -m pipeline',
                                     description = __doc__)
    
    

if __name__ == '__main__':
    _launch()