pyinstaller --onefile cli.py --add-data data:data
RD /S /Q "/build"
del "cli.spec"