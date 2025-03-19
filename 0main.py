import json, os, csv, inspect
from datetime import datetime
import time, sys, shutil
from pathlib import Path
import pandas as pd, yfinance as yf, finnhub
import psutil, platform,subprocess


def load_txt_file(txt_file):
    #content = load_txt_file("file.txt")
    with open(txt_file, 'r') as file:
        content = file.read()  # Read the entire content of the file
    return content
def write_txt_file(txt_file,content):
    #write_txt_file("file.txt",content)
    with open(txt_file, 'w') as file:
        file.write(content)
        file.close()

def csv_to_book(file_to_load):
    #list = csv_to_book("0upcoming.csv")
    with open(file_to_load, 'r') as f:
        reader = csv.DictReader(f)        
        loaded_list = list(reader)
    return(loaded_list)
def book_to_csv(book,output_file):
    #book_to_csv(dictionary,"0upcoming.csv")
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=book[0].keys())
        writer.writeheader()
        writer.writerows(book)

def copy_to_main():
    import shutil
    # Specify the source and destination files
    source_file = '0main.py'
    destination_file = 'main.py'
    # Copy the contents from the source file to the destination file
    shutil.copy(source_file, destination_file)
    print(f"Contents of {source_file} have been copied to {destination_file}.")

def create_if_not_exist():
    cwd = os.getcwd()
    files = os.listdir(cwd)
    create = []
    create.append("0sec_no_return.txt")
    create.append("sec-edgar-filings")
    create.append("finnhub-earnings")
    for check in create:
        if check not in files:
            if ".txt" in check:
                with open(check, 'w') as file:
                    pass  # The file is now created or emptied (if it already existed)
            if '.' not in check:
                os.makedirs(check, exist_ok=True)
    

def get_finnhub_earnings(finnhub_folder,start_date,end_date):
    #get_finnhub_earnings("finnhub_earnings",start_date,end_date)
    cwd = os.getcwd()
    finnhub_directory = os.path.join(cwd, finnhub_folder)
    finnhub_list = os.listdir(finnhub_directory)
    finnhub_file_name = start_date+"."+end_date+".json"
    if finnhub_file_name not in finnhub_list:
        finnhub_client = finnhub.Client(
            api_key="cupjchpr01qk8dnkc8qgcupjchpr01qk8dnkc8r0")
        #print(finnhub_client.earnings_calendar(_from="2025-02-18", to="2025-02-18", symbol="", international=False))
        future_earnings = finnhub_client.earnings_calendar(_from=start_date,
                                                  to=end_date,
                                                  symbol="",
                                                  international=False)
        # Save the response to a JSON file
        output_file = os.path.join(finnhub_directory, finnhub_file_name)
        with open(output_file, 'w') as json_file:
            json.dump(future_earnings, json_file, indent=4)
        print("Earnings data has been saved to " + output_file + ".json")
        print("request made")
    else:
        print("already exists",finnhub_file_name)

def stocks_from_finnhub_data(finnhub_file,stock_name_file,upcoming_file):
    # Open and load JSON file
    with open(finnhub_file, 'r') as file:
        finn_data = json.load(file)
    # Print the loaded dictionary
    finn_data2 = finn_data["earningsCalendar"]
    output = []
    stock_name_list = csv_to_book(stock_name_file)    
    for item in finn_data2:
        symbol = item["symbol"]
        date = item["date"]
        new={}    
        new['symbol'] = symbol
        new['date'] = date
        new['name'] = ""
        for stock in stock_name_list:
            #print(stock)
            if symbol==stock["Ticker"]:
                new['name'] = stock["Name"]
                continue
        output.append(new)
    for item in output:
        print(item)
    print("finnhub_file",finnhub_file)
    print(str(len(output))+" stocks in file")
    if len(output)==0:
        print("no stocks in file, no stocks for date")
        print("aborting process/operations")
        sys.exit()
    with open(upcoming_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=output[0].keys())
        writer.writeheader()
        writer.writerows(output)
def most_vol_pri(list_length,file_vol_pri,file_upcoming):
    with open(upcoming_file, 'r') as f:
        reader = csv.DictReader(f)        
        list_upcoming = list(reader)
    with open(file_vol_pri, 'r') as f:
        reader = csv.DictReader(f)        
        list_vol_pri = list(reader)
    redone = []
    for check_upcoming in list_upcoming:
        new_item = {}
        new_item["vol*pri"]=0
        for check_vp in (list_vol_pri):
            if check_upcoming["symbol"]==check_vp["Symbol"]:
                new_item["vol*pri"]=check_vp["vol*pri"]
        new_item["symbol"]=check_upcoming["symbol"]
        new_item["date"]=check_upcoming["date"]
        new_item["name"]=check_upcoming["name"]
        #item = new_item
        #print(item)
        redone.append(new_item)
    redone = sorted(redone, key=lambda x: float(x["vol*pri"]),reverse=True)
    redone = redone[0:list_length]
    book_to_csv(redone,file_upcoming)
    redone.reverse()
    for item in redone:
        print(item)
    #sys.exit()

def get_sec_earn_dates(match_file):
    look_at = []
    with open(match_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            look_at.append(row)  # Add each row to the list
    #get earnings dates
    from pathlib import Path
    cwd = os.getcwd()
    edgar_folder = os.path.join(cwd,"sec-edgar-filings")
    edgar_stocks = os.listdir(edgar_folder)  
    from sec_edgar_downloader import Downloader
    dl = Downloader("MyCompanyName", "my.email@domain.com")
    print(edgar_stocks)
    stocks = csv_to_book(match_file)
    sec_no_data_file = "0sec_no_data.csv"
    sec_no_data_list = csv_to_book(sec_no_data_file)
    print(stocks)
    upload_counter = 0
    iden_codespace = "codespace"
    iden_laptop = "???"
    laptop_or_codespace = platform.node()
    for val in stocks:
        check_stock = val["symbol"]
        stock = check_stock
        symbol = stock
        match = 0
        for item in sec_no_data_list:
            check = item["sec_no_data"]
            if check==symbol:
                match=1
                break
        if match==1:
            continue
        if check_stock in edgar_stocks:
            k8_folder = os.path.join(edgar_folder,stock,"8-K")    
            k8_date_list = os.listdir(k8_folder)
            number_of_dates = len(k8_date_list)
            if number_of_dates>30:
                folder_delete = os.path.join(edgar_folder,stock)
                print(number_of_dates,stock,"will delete = "+folder_delete)
                print("number of dates = "+str(number_of_dates))
                shutil.rmtree(folder_delete)
            #will go to next stock because it is already there..
            #will not have to overwrite..
            else:
                continue 
        index = stocks.index(val)
        print(index,len(stocks),"stock = "+check_stock)
        stock_folder = os.path.join(edgar_folder,stock,"8-K")
        #print(stock_folder)
        print("8k attempt for "+symbol)
        print("upload_counter="+str(upload_counter))
        try:
            dl.get("8-K", symbol)
        except Exception as e:
            print(f"Error Type: {type(e).__name__}")
            no_data_add_to_sec = {}
            no_data_add_to_sec["sec_no_data"]=symbol
            sec_no_data_list.append(no_data_add_to_sec)
            book_to_csv(sec_no_data_list,sec_no_data_file)
            continue
        try:
            earn_dates = os.listdir(stock_folder)
        except:
            #sec_no_data_list = sec_no_data_list+"\n"+symbol
            no_data_add_to_sec = {}
            no_data_add_to_sec["sec_no_data"]=symbol
            sec_no_data_list.append(no_data_add_to_sec)
            book_to_csv(sec_no_data_list,sec_no_data_file)
            #write_txt_file(sec_no_data_file,sec_no_data_list)            
            continue
        print(earn_dates) 
        keep_years = ["-20-","-21-","-22-","-23-","-24-","-25-"]
        for b,date in enumerate(earn_dates):
            print(len(look_at),b,len(earn_dates))
            match = 0
            for year in keep_years:
                if year in date:
                    match = match+1
            print("match",match)
            if match==0:
                to_delete = os.path.join(stock_folder,date)
                print(to_delete)
                shutil.rmtree(to_delete)
        earn_dates = os.listdir(stock_folder)
        for b,date in enumerate(earn_dates):
            #print(len(look_at),b,len(earn_dates))
            check_file = os.path.join(stock_folder,date,"full-submission.txt")
            print(check_file)
            with open(check_file, 'r') as file:
                content = file.read()  # Read the entire content of the file
                to_delete = os.path.join(stock_folder,date)            
                if "ITEM INFORMATION:		Results of Operations and Financial Condition" in content:
                    if "ITEM INFORMATION:		Financial Statements and Exhibits" in content:
                        count_earn_lower = content.count("earn")
                        count_earn_upper = content.count("Earn")
                        count_earn_total = count_earn_lower+count_earn_upper
                        print("count_earn_lower",count_earn_lower)
                        print("count_earn_upper",count_earn_upper)
                        print("count_earn_total",count_earn_total)
                        #put earn count amount at top of text when redo it
                        #might have to change this down to 2 or something..
                        if count_earn_total>2: 
                            #might have to change this down to 2 or something..
                            content = str(count_earn_total)+"\n"+content
                            with open(check_file, 'w') as file:
                                file.write(content[0:20000])                        
                            continue
    
                file.close()        
                print("deleting= "+to_delete)
                shutil.rmtree(to_delete)

        earn_dates_check = os.listdir(stock_folder)
        if earn_dates_check==0:                        
            #redo..but then just do a search for 1 earn value..
            meow="meow"
        upload_counter+=1
        if upload_counter % 10 == 0:
            if iden_codespace in laptop_or_codespace:
                subprocess.run(['python', '0push_codespace_to_repo.py'])
            if iden_laptop in laptop_or_codespace:    
                subprocess.run(['python', '0push_laptop_to_repo.py'])

def get_yahoo_history(upcoming_file):
    # Open the CSV file and load it as a dictionary
    with open(upcoming_file, 'r') as f:
        reader = csv.DictReader(f)        
        upcoming = list(reader)
    # Print the loaded data
    print(upcoming)
    cwd = os.getcwd()
    file_list = os.listdir(cwd)
    for item in upcoming:
        symbol = item["symbol"]
        date = item["date"]
        check_file=symbol+"-history.csv"
        if check_file in file_list:
            continue
        data = yf.download(symbol, period="5y", interval="1d").sort_index(ascending=False)
        data.columns = data.columns.get_level_values(0)  # Remove multi-index headers
        # Move "Open" to the second column and round all float values to 2 decimal places
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']].round(2)
        data.to_csv(symbol+'-history.csv', index_label='Date')
        print(symbol+'-history.csv'+" saved")
        print(upcoming.index(item),len(upcoming))
        time.sleep(2)
    #gen list
    compare = []
    for item in upcoming:
        symbol = item["symbol"]
        print(symbol)
        load_file = symbol+"-history.csv"
        with open(load_file, 'r') as f:
            reader = csv.DictReader(f)        
            prices = list(reader)     
            #print(prices)
        print(load_file)
        index = upcoming.index(item)
        #if index<55:
        #    continue
        with open(load_file, mode='r') as file:
            reader = csv.DictReader(file)  # Reads CSV as a list of dictionaries
            data = list(reader)
        try:
            price = float(data[0]["Close"])
        except:
            continue
        volume = float(data[0]["Volume"])
        volpri = int(price*volume)
        new = {}
        new["vol*pri"] = volpri
        new["symbol"] = symbol
        new["date"] = date
        new["name"]=""
        try:
            new["name"]=item["name"]
        except:
            continue
        #new["name"] = item["Name"]
        print("new",new)
        compare.append(new)
    compare = sorted(compare, key=lambda x: float(x["vol*pri"]),reverse=True)
    print(compare)
    with open(compare_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=compare[0].keys())
        writer.writeheader()
        writer.writerows(compare)

def prices_around_earnings(match_file,required_ratio,folder_analysis):
    stock_list = csv_to_book(match_file)
    cwd = os.getcwd()
    edgar_folder = os.path.join(cwd,"sec-edgar-filings")          
    continue_pattern= []
    reverse_pattern=[]
    #con_rev={}
    con_rev=[]
    final_cr = []
    final_cr2 = []
    for specific in stock_list:
        print(specific)
        symbol = specific["symbol"]
        stock = specific["symbol"]
        name = specific["name"]
        stock_data= ""
        print(symbol)
        print(stock_list.index(specific),len(stock_list))
        k8_dir = os.path.join(edgar_folder,stock,"8-K")  
        try:
            k8_list = os.listdir(k8_dir)
        except:
            continue
        earnings_dates = []
        date_identifier = "DATE AS OF CHANGE:"
        for k8_code in k8_list:
            if "-25-" not in k8_code and "-24-" not in k8_code and "-23-" not in k8_code: 
                continue
            file_to_load = os.path.join(k8_dir,k8_code,"full-submission.txt")    
            with open(file_to_load, 'r') as file:
                content = file.read()
                if "Results of Operations and Financial Condition" in content and "Financial Statements and Exhibits" in content:
                    what_to_find = date_identifier
                    dates_start = content.find(what_to_find)
                    date_end = content.find("\n",dates_start)
                    date = content[dates_start:date_end]
                    earnings_dates.append(date)
        earnings_dates.sort()
        earnings_dates.reverse()
        earnings_dates=earnings_dates[0:8]
        earnings_dates.reverse()
        #print(earnings_dates)
        earnings_dates1 = earnings_dates
        earn_dates2 = []
        for date in earnings_dates1:
            new = date.replace(date_identifier,"")
            new = new.replace("\t","")
            earn_dates2.append(new)
        dates_list = earn_dates2
        object_current_datetime = datetime.now()    
        list_prices = []
        prices_file = symbol + "-history.csv"
        with open(prices_file, mode='r') as file:
            csv_reader = csv.DictReader(file)
            list_prices = [row for row in csv_reader]   
        continue_list=  []
        reverse_list = []
        continue_dictionary= {}
        reverse_dictionary = {}
        more = {}
        stock_cr = []
        ratios_up_vs_down = []
        #for date in dates_list:
        #    print("date look for=",date)
        direction_close=""
        for specific_date in dates_list:
            #print("specific_date",specific_date)
            days_surrounding = {}
            for day_prices in list_prices:
                try:
                    day_prices["Date"] = day_prices["Date"].replace("-","")
                except:
                    print("day_prices",day_prices)
                if specific_date in day_prices["Date"]:
                    index_before=list_prices.index(day_prices)+1
                    index_after=list_prices.index(day_prices)-1
                    day_before = list_prices[index_before]
                    day_listed = day_prices
                    day_after = list_prices[index_after]
                    max_vol = ""
                    vol_day_of = int(day_listed["Volume"])
                    vol_day_after = int(day_after["Volume"])                  
                    if vol_day_of>vol_day_after:
                        max_vol = day_listed
                    if vol_day_of<vol_day_after:
                        max_vol = day_after
                    days_surrounding["before"]=day_before
                    days_surrounding["day_of"]=day_listed
                    days_surrounding["after"]=day_after
            for key, day in days_surrounding.items():
                #print(key,day)
                if max_vol==day:
                    for key_other, out in days_surrounding.items():
                        print(symbol,key_other,out)
                        stock_data+=str(out)+"\n"
                    print("max_vol",max_vol)
                    get_close=""
                    if key=="after":
                        get_close = "day_of"
                    if key=="day_of":
                        get_close = "before"
                    values = {}
                    close_day_before = float(days_surrounding[get_close]["Close"])
                    values["close"] = close_day_before
                    morning = float(day["Open"])
                    values["open"] = morning
                    gap = round(float(((morning/close_day_before)-1)*100),2)
                    values["gap"]=gap
                    day_high = float(day["High"])
                    day_low = float(day["Low"])
                    day_low = float(day["Low"])
                    close = float(day["Close"])                    
                    same_direction=""
                    opposite_direction=""
                    if gap>0:
                        same_direction=day_high
                        opposite_direction=day_low
                    if gap<0:
                        same_direction=day_low
                        opposite_direction=day_high
                    values["same"]=same_direction
                    values["oppo"]=opposite_direction
                    stock_data+=str(values)+"\n"
                    print("values",values)
                    if gap==0:
                        print("gap=0, abort!")
                        continue
                    percent_continue = abs(float(int(((same_direction/morning)-1)*10000)/100))
                    percent_reverse = abs(float(int(((opposite_direction/morning)-1)*10000)/100))
                    more_data = {}
                    more_data["percent_continue"]=percent_continue
                    more_data["percent_reverse"]=percent_reverse
                    stock_data+=str(more_data)+"\n"
                    if percent_continue==0:
                        percent_continue=1
                    if percent_reverse==0:
                        percent_reverse=1
                    ratio_continue= abs(percent_continue/percent_reverse)
                    ratio_reverse= abs(percent_reverse/percent_continue)
                    ratio_continue= float(int(ratio_continue*100)/100)
                    ratio_reverse= float(int(ratio_reverse*100)/100)
                    new = {}
                    new["Date"]=day["Date"]
                    if ratio_continue>ratio_reverse:
                        new["Direction"]="C"
                        new["Amount"]=ratio_continue
                    if ratio_reverse>ratio_continue:
                        new["Direction"]="R"
                        new["Amount"]=ratio_reverse
                    if ratio_continue==ratio_reverse:
                        new["Direction"]="E"
                        new["Amount"]=ratio_continue
                    close_move = round(float(((close/morning)-1)*100),2)                       
                    if gap>0 and close_move>0:
                        direction_close+="C"
                    if gap>0 and close_move<0:
                        direction_close+="R"
                    if gap<0 and close_move>0:
                        direction_close+="R"
                    if gap<0 and close_move<0:
                        direction_close+="C"
                    stock_data+=str(new["Direction"])+"\n"
                    stock_data+="close_move = "+str(close_move)+"\n"                    
                    stock_data+="\n"
                    print("gap",gap)
                    stock_cr.append(new)
                    move_up = round(float(((day_high/morning)-1)*100),2)
                    move_down = round(float(((day_low/morning)-1)*100),2)
                    try:
                        up_down_ratio = (move_up/move_down)
                    except ZeroDivisionError:
                        up_down_ratio=move_up
                    try:
                        down_up_ratio = (move_down/move_up)
                    except ZeroDivisionError:
                        up_down_ratio=move_down
                    max_ratio = max(up_down_ratio,up_down_ratio)
                    ratios_up_vs_down.append(max_ratio)
        stock_cr.sort(key=lambda x: x["Date"])
        #ratios_up_vs_down.sort()
        try:
            uvd = min(ratios_up_vs_down)
            uvd = round(uvd,2)
        except:
            uvd = "---"
        cr_string = ""
        for item in stock_cr:
            cr_string=cr_string+item["Direction"]
            #print("item",item)
        if len(stock_cr)==0:
            continue
        #min_value=stock_cr[0]["Amount"]
        min_value = min(stock_cr, key=lambda x: x['Amount'])["Amount"]
        print("min_value",min_value)
        min2= int((min_value-1)*100)
        #if min2>required_ratio:
        if min2>0: 
            new = {}
            new["sym"]=symbol
            new["CvR"]=cr_string
            new["OvC"]=direction_close
            new["ratio"]=min2
            print("specific",specific)
            new["v*p"]=int(float(specific["vol*pri"]))
            new["name"]=name[0:10]
            new["uvd"]=uvd
            new["date"]=specific["date"]
            final_cr2.append(new)
            folder_analysis = os.path.join(cwd,folder_analysis)
            data_file = os.path.join(folder_analysis,symbol+".txt")
            to_write=""
            #for key, data in new.items():
            #    to_write+=str(key)+":"+str(data)+"\n"
            write_txt_file(data_file,stock_data)

        #stop at specific stock
        #leave =="" if you just want it to run
        if symbol=="":
            sys.exit()
    final = sorted(final_cr2,key=lambda x: x["v*p"])
    same_direction = []
    for item in final:
        direction = item["CvR"]
        if "CCCCCCCC" in direction or "RRRRRRRR" in direction:
            same_direction.append(item)
    final = final+same_direction
    for item in final:
        print("item",item)

def specific_day(start_day,end_day, file_to_load,folder_analysis):
    list = []
    with open(file_to_load, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(row)  # Add each row to the list
    correct_date = []
    from datetime import datetime, timedelta
    start_date_str = start_day
    end_date_str = end_day
    start_date_obj = datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date_obj = datetime.strptime(end_date_str, "%Y-%m-%d")
    for a,val in enumerate(list):
        if a==0:
            continue
        check_date_str = val[3]   
        check_date_obj = datetime.strptime(check_date_str, "%Y-%m-%d")
        if check_date_obj>=start_date_obj:
             if check_date_obj<=end_date_obj:
                correct_date.append(val)
    correct_date = correct_date[0:30]
    for a,val in enumerate(correct_date):
        print("val",val)    

required_ratio=100
finnhub_folder = "finnhub-earnings"
upcoming_file = "0upcoming_earnings.csv"
stock_name_file = "0stock_names.csv"
compare_file = "0compare.csv"
google_vp_file = "0vp_google_data.csv"
history_header = [["date","open","high","low","close","volume"]]
match_file = "0match.csv"
file_vol_pri = "0vol_pri_list.csv"
folder_analysis = "data_around_earnings"

finnhub_start = "2025-03-17"
finnhub_end = "2025-06-17"
list_length = 150
finnhub_file = os.path.join(finnhub_folder,finnhub_start+"."+finnhub_end+".json")

create_if_not_exist()
get_finnhub_earnings(finnhub_folder,finnhub_start,finnhub_end)
stocks_from_finnhub_data(finnhub_file,stock_name_file,upcoming_file)
most_vol_pri(list_length,file_vol_pri,upcoming_file)
get_yahoo_history(upcoming_file)
get_sec_earn_dates(upcoming_file)
prices_around_earnings(upcoming_file,required_ratio,folder_analysis)
"""
#specific_day(start_date,end_date, match_file)
"""
#last updated=2025-03-19 21:14:13----------