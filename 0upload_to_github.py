from github import Github
import os
token_file_location = "C:\\Users\\--\\0code\\00token_github.txt"
with open(token_file_location, 'r') as file:
    token = file.read()
#token = "YOUR_GITHUB_TOKEN"
g = Github(token)
repo_name = "violin788/0code"
repo = g.get_repo(repo_name)
code0_directory = "C:\\Users\\--\\0code"
code0_list = os.listdir(code0_directory)
for specific in code0_list:
    file_path = os.path.join(code0_directory,specific)
    if "token" in file_path:
        continue
    #file_path = "path/to/your/file.txt"
    file_name = os.path.basename(file_path)
    branch = "main"
    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        file_content = file.read()
    repo_file_path = f"{file_name}"
    try:
        try:
            existing_file = repo.get_contents(repo_file_path, ref=branch)
            repo.update_file(existing_file.path, "Updating file", file_content, existing_file.sha, branch=branch)
            print(f"File '{file_name}' updated in '{repo_name}' repository.")
            print(code0_list.index(specific),len(code0_list))       
        except:
            repo.create_file(repo_file_path, "Adding new file", file_content, branch=branch)
            print(f"File '{file_name}' uploaded to '{repo_name}' repository.")
    except Exception as e:
        print(f"An error occurred: {e}")
