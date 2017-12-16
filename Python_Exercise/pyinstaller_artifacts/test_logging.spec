# -*- mode: python -*-

block_cipher = None

a = Analysis(['..\\pythonpractice\\test_logging.py'],	## more scripts can be added to the list (no tuples), format:['script1', 'script2', ...]
             pathex=['..\\pythonpractice', '..\\tools', 'C:\\Users\\marashid\\Documents\\Personal_Stuff\\Personal Training and Development\\Python\\Python_Exercise\\pyinstaller_artifacts'],
             binaries=[],
             datas=[('..\\pythonpractice\\Logs\\*.log', '.\\copied_logs\\')],	## more tuples of data can be added to the list, format:[('current location of data file(s)', 'location to contain data file(s) at run time')]
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

## further data files can be added but each will have to be added separately in tuples, i.e. no wildcard usage for enmass addition
a.datas += [('.\\test files\\testfile1.txt', '..\\pythonpractice\\test files\\testfile1.txt', 'DATA')]	## format:['run-time name', 'full path in build', 'typecode']

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='test_logging',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='test_logging')
