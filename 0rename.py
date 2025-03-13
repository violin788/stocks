import os
cwd = os.getcwd()
#directory = os.path.join(cwd,"sec-edgar-filings")
edgar_folder = "sec-edgar-filings"
in_edgar = os.listdir(edgar_folder)
print(in_edgar)
for stock in in_edgar:
    k8_folder = os.path.join(edgar_folder,stock,"8-K")
    print(k8_folder)
    k8_dates=  os.listdir(k8_folder)
    print(k8_dates)
    for k8_name in k8_dates:
        k8_specific = os.path.join(k8_folder,k8_name,"full-submission.txt")
        with open(k8_specific, 'r') as file:
            content = file.read()  # Read the entire content of the file
            shortened = content[0:3000]
            with open(k8_specific, 'w') as file2:
                file2.write(content[0:3000])

            print(shortened)


"""
for item in in_folder:
    folder = os.path.join(directory,item,"8-K")
    in_local_dir = os.listdir(folder)
    if "." in item:
        continue
    print(item)
    print(in_local_dir)"
    """