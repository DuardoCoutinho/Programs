import sys
from cx_Freeze import setup, Executable


base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("comparador.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["sqlite3", "os", "xlstocsv"],
        include_files = ["usuarios.db", "Relatorio.Customizado.GUID.9.xls", "xlstocsv.py"],
        excludes = []
)




setup(
    name = "Script",
    version = "1.0",
    description = "Script para criação de usuarios no dominio",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
