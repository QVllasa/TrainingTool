# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\qendrimvllasa\\Desktop\\TrainingTool'],
             binaries=[],
             datas=[
              ("misc/Siemens_Sans/SISAN03.ttf","misc/Siemens_Sans/"),
             ("misc/Siemens_Sans/SISAN06.ttf","misc/Siemens_Sans/"),
             ("misc/Siemens_Sans/SISAN08.ttf","misc/Siemens_Sans/"),
             ("misc/Siemens_Sans/SISAN33.ttf","misc/Siemens_Sans/"),
             ("misc/Siemens_Sans/SISAN36.ttf","misc/Siemens_Sans/"),
             ("misc/Siemens_Sans/SISAN38.ttf","misc/Siemens_Sans/"),
             ("icon.ico",'.')



             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Training Tool',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='icon.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Training Tool')
