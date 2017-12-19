# -*- mode: python -*-

block_cipher = None

a = Analysis(['..\\tools\\backup_my_listed_files_to_drpbx.py'],
             pathex=['.\\pyinstaller_artifacts', '..\\Python_Exercise\\tools', '..\\Python_Exercise\\pythonpractice'],
             binaries=[],
             datas=[('..\\tools\\data_files\\*.*', '.\\data_files\\')],
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
          name='backup_my_listed_files_to_drpbx',
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
               name='backup_my_listed_files_to_drpbx')
