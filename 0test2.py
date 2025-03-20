import json, os, csv, inspect
from datetime import datetime
import time, sys, shutil
from pathlib import Path
import pandas as pd, yfinance as yf, finnhub
import psutil, platform,subprocess


#folder_history.append"sec-edgar-filings2"
ranges_history = []
ranges_history.append(["A","D"])
ranges_history.append(["E","H"])
ranges_history.append(["I","L"])
ranges_history.append(["M","P"])
ranges_history.append(["Q","T"])
ranges_history.append(["U","Z"])
cwd = os.getcwd()
history_folder = os.path.join(cwd,"history-yahoo") 

ranges_history = []
ranges_history.append(["A","D"])
ranges_history.append(["E","H"])
ranges_history.append(["I","L"])
ranges_history.append(["M","P"])
ranges_history.append(["Q","T"])
ranges_history.append(["U","Z"])
cwd = os.getcwd()
history_folder = os.path.join(cwd,"history-yahoo") 

def history_load(subfolders,symbol,ending):
    #prices = history_load(ranges_history,symbol,"-history.csv")
    cwd = os.getcwd()
    check_letter=  symbol[0]
    for range in ranges_history:
        if range[0] <= check_letter <= range[1]:
            print(range)
            break
    folder_load = "history-yahoo-"+range[0]+"-"+range[1]
    print(folder_load)
    file_open = os.path.join(history_folder,folder_load,symbol+ending) 
    print(file_open)
    loaded_csv = csv_to_book(file_open)
    return loaded_csv

def history_save(data,symbol,ending):
    #history_save(data,symbol,"-history.csv")
    check_letter=  symbol[0]
    for range in ranges_history:
        if range[0] <= check_letter <= range[1]:
            print(range)
            break
    folder_save = "history-yahoo-"+range[0]+"-"+range[1]
    print(folder_load)
    file_save = os.path.join(cwd,folder_save,symbol+ending) 
    print(file_save)
    data.to_csv(file_save, index_label='Date')