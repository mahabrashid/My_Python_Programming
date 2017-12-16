# -*- mode: python -*-

block_cipher = None


a = Analysis(['..\\pythonpractice\\hello_you.py'],
             pathex=['..\\pythonpractice', '..\\tools', 'C:\\Users\\marashid\\Documents\\Personal_Stuff\\Personal Training and Development\\Python\\Python_Exercise\\pyinstaller_artifacts'],
             binaries=[],
             datas=[('..\\pythonpractice\\test files\\testfile1.txt', '.\\test files')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='hello_you',
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
               name='hello_you')
