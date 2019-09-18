# -*- mode: python -*-

block_cipher = None


a = Analysis([
'sysrun.py',
'UIForms\\ui_about.py',
'UIForms\\ui_add_method.py',
'UIForms\\ui_chgpwd.py',
'UIForms\\ui_chguser.py',
'UIForms\\ui_login.py',
'UIForms\\ui_mainwindow.py',
'UIForms\\ui_new_unpass.py',
'UIForms\\ui_part_need_review.py',
'UIForms\\ui_parts_idea.py',
'UIForms\\ui_plot_item.py',
'UIForms\\ui_qa_data.py',
'Basic\\getdb.py',
'Basic\\report.py',
'Basic\\user_info.py',
'UserInterface\\add_method.py',
'UserInterface\\chgpwd.py',
'UserInterface\\chguser.py',
'UserInterface\\mainwindow.py',
'UserInterface\\new_unpass.py',
'UserInterface\\parts_idea.py',
'UserInterface\\plot_item.py',
'UserInterface\\qa_data.py'
],
             pathex=['F:\\python_work\\PartsReview'],
             binaries=[],
             datas=[
             (r'F:\python_work\PartsReview\icons', 'icons'),
             (r'F:\python_work\PartsReview\Configration', 'Configration'),
             (r'F:\python_work\PartsReview\output', 'output'),
             (r'F:\python_work\PartsReview\fonts', 'fonts')
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
          name='GotoReview',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          icon='icons\\Quality_Control_72px.ico',
          console=False)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='GotoReview')
