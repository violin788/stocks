import os
import shutil
cwd = os.getcwd()
edgar_folder = os.path.join(cwd, "sec-edgar-filings")
stock_list = os.listdir(edgar_folder)
zero = []
under = []
twenty = []
over_20 = []
for stock in stock_list:
    k8_directory = os.path.join(edgar_folder,stock,"8-K")
    try:
        k8_files = os.listdir(k8_directory)
    except:
        #eventually delete the directory that has 0
        continue
    k8_count = len(k8_files)
    data = {}
    data["stock"]=stock
    data["k8_count"]=k8_count
    if k8_count==0:
        zero.append(data)    
    if k8_count==20:
        twenty.append(data)
    if k8_count>0 and k8_count<20:
        under.append(data)
    if k8_count>20:
        over_20.append(data)
    #print(stock,k8_count)
    #print("under")
amounts = {}
amounts["zero"]=zero
amounts["under"]=under
amounts["twenty"]=twenty
amounts["over_20"]=over_20
for key,data  in amounts.items():
    print(key)
    for item in data:
        print(key,item)
    continue
    """
    if key=="zero":
        folder_delete = os.path.join(edgar_folder,item["stock"])
        shutil.rmtree(folder_delete) 
        """