
def csv_to_book(file_to_load):
    #list = csv_to_book("0upcoming.csv")
    with open(file_to_load, 'r') as f:
        reader = csv.DictReader(f)        
        loaded_list = list(reader)
    return(loaded_list)


import os,shutil
import sys,csv
#folder_history.append"sec-edgar-filings2"
ranges = []
ranges.append(["A","D"])
ranges.append(["E","H"])
ranges.append(["I","L"])
ranges.append(["M","P"])
ranges.append(["Q","T"])
ranges.append(["U","Z"])
cwd = os.getcwd()
history_folder = os.path.join(cwd,"history-yahoo") 

def history_load(subfolders,symbol,ending):
    #prices = history_load(ranges,symbol,"-history.csv")
    cwd = os.getcwd()
    check_letter=  symbol[0]
    for range in ranges:
        if range[0] <= check_letter <= range[1]:
            print(range)
            break
    folder_load = "history-yahoo-"+range[0]+"-"+range[1]
    print(folder_load)
    file_open = os.path.join(history_folder,folder_load,symbol+ending) 
    print(file_open)
    loaded_csv = csv_to_book(file_open)
    return loaded_csv

prices = history_load(ranges,"ADBE","-history.csv")
print(prices)