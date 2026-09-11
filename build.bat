pyinstaller --onefile cli.py --add-data data:data
rd /s /q "build"
del "cli.spec"