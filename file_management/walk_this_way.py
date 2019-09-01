import os

path = "c:/zzSftwr"
dvdr = "\n----------"
# i = 0
for (path, dirs, files) in os.walk(path):
    print("path", path, dvdr)
    print("Directories", dirs, dvdr)
    print("Files", files, dvdr)
