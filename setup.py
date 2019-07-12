import os

if(os.name == "Darwin"):
    os.system("sh setup.py")
elif os.name == "Windows":
    os.system("\\setup.bat")