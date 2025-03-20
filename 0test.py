import os 

def csv_to_book(file_to_load):
    #list = csv_to_book("0upcoming.csv")
    with open(file_to_load, 'r') as f:
        reader = csv.DictReader(f)        
        loaded_list = list(reader)
    return(loaded_list)


def history_save(data,symbol,ending):
    #history_save("CVS","-history.csv")
    cwd = os.getcwd()
    check_letter=  symbol[0]
    if 'A' <= check_letter <= 'M':
        print("AM")
        folder_save = "history-yahoo-A-M"
    if 'N' <= check_letter <= 'Z':
        print("NZ")
        folder_save = "history-yahoo-N-Z"
    file_save = os.path.join(cwd,folder_save,symbol+ending) 
    book_to_csv(data,file_save)

import csv
def history_load(symbol):
    cwd = os.getcwd()
    #history_load("CVS"):
    check_letter=  symbol[0]
    if 'A' <= check_letter <= 'M':
        print("AM")
        folder_load = "history-yahoo-A-M"
    if 'N' <= check_letter <= 'Z':
        print("NZ")
        folder_load = "history-yahoo-N-Z"
    file_open = os.path.join(cwd,folder_load,symbol+"-history.csv") 
    print(file_open)
    loaded_csv = csv_to_book(file_open)
    return loaded_csv

test = history_load("COE")
print(test)