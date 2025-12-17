import os
from datetime import datetime
import subprocess

cwd = os.getcwd()
print(cwd)

# os.chdir("/tmp")
# print(os.getcwd())

os.mkdir("logs")
os.rmdir("logs")

with open("test.txt", "w") as f:
    f.write("Testing")

if os.path.exists("test.txt"):
    print("File exists")
    info = os.stat("test.txt")
    print(info.st_size)
    change = datetime.fromtimestamp(info.st_mtime)
    print(change.strftime('%Y-%m-%d %H:%M:%S'))


# os.remove("test.txt")

# os.system("ls -la")


try:
    result = subprocess.run(["ls", "-la"], capture_output=True, text=True, check=True)
    print(result.stdout)
except FileNotFoundError:
    print("No file found")
except subprocess.CalledProcessError as e:
    print(e)

