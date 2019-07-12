import os

print(f"Setting up for {os.name}")
if(os.name == "Darwin" or os.name == "posix"):
    os.system("sh setup.sh")
elif os.name == "Windows":
    os.system("\\setup.bat")
