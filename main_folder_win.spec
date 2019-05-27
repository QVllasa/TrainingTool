# -*- mode: python -*-

block_cipher = None


a = Analysis(['main_windows.py'],
             pathex=['/Users/qendrimvllasa/Library/Mobile Documents/com~apple~CloudDocs/Projects/Password Manager'],
             binaries=[('webdriver/windows/chromedriver.exe', 'webdriver/windows'),
             ('webdriver/windows/geckodriver.exe', 'webdriver/windows')],
             datas=[('C:/Users/qendrimvllasa/Anaconda3/Lib/site-packages/docx/templates/default.docx', "docx/templates"),('mdsp_password_manager.ico','.')
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
          name='Password Manager',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='mdsp_password_manager.ico' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Password Manager')
