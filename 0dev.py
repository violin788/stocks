
import os,shutil

cwd = os.getcwd()
edgar_folder = os.path.join(cwd,"sec-edgar-filings")          
edgar_list = os.listdir(edgar_folder)

for stock in edgar_list:
    k8_folder = os.path.join(edgar_folder,stock,"8-K")
    k8_date_list = os.listdir(k8_folder)
    number_of_dates = len(k8_date_list)
    if number_of_dates>20:
        print(number_of_dates,stock)
        folder_delete = os.path.join(edgar_folder,stock)
        shutil.rmtree(folder_delete)