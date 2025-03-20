import os,shutil

cwd = os.getcwd()
files = os.listdir(cwd)
#print(files)
for file in files:
    if "-history.csv" in file:
        print(file)
        os.remove(file)
        #dst_file = os.path.join(cwd,"history-yahoo",file)
        #print(dst_file)

        #shutil.copy(file, dst_file)