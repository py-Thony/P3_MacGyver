import sys
import os.path
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["os"], include_files = ["Data", "pics", "sound"], excludes = [
    "http", "email", "html", "asyncio", "concurrent", "ctypes", "lib2to3", "logging", "tkinter"])

base = None
if sys.platform == "win32":
    base = "Win32GUI"



executables = [Executable('Macgyver.py', base=base)]

setup(name='LabMac',
      version = '2.0',
      copyright= "Copyright © 2020 py_thony",
      description = 'Aidez MacGyver a sortir du labyrinthe',
      options = dict(build_exe = buildOptions),
      executables =[Executable("Macgyver.py", base=base)])
