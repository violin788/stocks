import os

def write_txt_file(txt_file,content):
    #write_txt_file("file.txt",content)
    with open(txt_file, 'w') as file:
        file.write(content)
        file.close()


cwd = os.getcwd()
edgar_folder = os.path.join(cwd,"sec-edgar-filings")          
edgar_list = os.listdir(edgar_folder)
for stock in edgar_list:
    k8_directory = os.path.join(edgar_folder,stock,"8-K")     
    try:
        k8_list = os.listdir(k8_directory)
    except:
        continue
    print(stock)
    print(k8_list)
    for k8_filing in k8_list:
        k8_file = os.path.join(k8_directory,k8_filing,"full-submission.txt")
        with open(k8_file, 'r') as file:
            content = file.read()
        #print(content)
        write_to = content[0:10000]
        write_txt_file(k8_file,write_to)
