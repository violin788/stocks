import os,shutil
cwd = os.getcwd()
folder_yahoo_history = os.path.join(cwd,"history-yahoo")
files = os.listdir(folder_yahoo_history)
#print(files)
for file in files:
    check_letter = file[0]
    print(file)
    print(check_letter)
    if 'A' <= check_letter <= 'M':
        print("AM")
        folder_dst = "history-yahoo-A-M"
    if 'N' <= check_letter <= 'Z':
        print("NZ")
        folder_dst = "history-yahoo-N-Z"
    file_src = os.path.join(folder_yahoo_history,file)
    file_dst = os.path.join(cwd,folder_dst,file) 
    print(file_src)
    print(file_dst)
    print("")
    shutil.copy(file_src, file_dst)
    #print(folder_dst)
    #print("")


    #os.remove(file)
    #dst_file = os.path.join(cwd,"history-yahoo",file)
    #print(dst_file)

    #shutil.copy(file, dst_file)