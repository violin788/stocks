import os,shutil
#folder_history.append"sec-edgar-filings2"
ranges = []
ranges.append(["A","D"])
ranges.append(["E","H"])
ranges.append(["I","L"])
ranges.append(["M","P"])
ranges.append(["Q","T"])
ranges.append(["U","Z"])
cwd = os.getcwd()
for item in ranges:
    print(item)
    folder_range = item[0]+"-"+item[1]
    folder_new = os.path.join(cwd,"sec-edgar-filings2","sec-edgar-filings2-"+folder_range)
    print(folder_new)
    #folder_new = 
    os.makedirs(folder_new, exist_ok=True)


#for 

#os.makedirs(check, exist_ok=True)