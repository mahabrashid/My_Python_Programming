'''
Created on 6 Nov 2017

@author: marashid
'''

''''
you can't do relative imports from the file you execute since __main__ module is not a part of a package.

Absolute imports - import something available on sys.path

Relative imports - import something relative to the current module, must be a part of a package
'''
print(__name__)

try:
    # Trying to find module in the parent package
    from . import config
    print(config.debug)
    del config
except ImportError:
    print('Relative import failed')

try:
    # Trying to find module on sys.path
    import config
    print(config.debug)
except ModuleNotFoundError:
    print('Absolute import failed')