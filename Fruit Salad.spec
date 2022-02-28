# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/Users/Timbu/Documents/GitHub/Fruit-Salad/Fruit Salad.py'],
             pathex=[],
             binaries=[],
             datas=[('C:/Users/Timbu/Documents/GitHub/Fruit-Salad/3060.ico', '.'), ('C:/Users/Timbu/Documents/GitHub/Fruit-Salad/fail.vbs', '.'), ('C:/Users/Timbu/Documents/GitHub/Fruit-Salad/MEGAGUIDE.mp3', '.'), ('C:/Users/Timbu/Documents/GitHub/Fruit-Salad/languages', 'languages/'), ('C:/Users/Timbu/Documents/GitHub/Fruit-Salad/GUI', 'GUI/'), ('C:/Users/Timbu/Documents/GitHub/Fruit-Salad/trex', 'trex/')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='Fruit Salad',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , uac_admin=True, icon='C:\\Users\\Timbu\\Documents\\GitHub\\Fruit-Salad\\3060.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Fruit Salad')
