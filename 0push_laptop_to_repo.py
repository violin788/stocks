import subprocess
import os,sys
from datetime import datetime
alter_files = []
alter_files.append("0main.py")
for specific in alter_files:
    now = datetime.now()
    time_new = now.strftime("%Y-%m-%d %H:%M:%S") 
    with open(specific, "r") as file:
        iden_start_time = "#last updated="
        iden_end_time = "----------"
        content = file.read()
        start_old_time_string = content.find(iden_start_time)
        end_old_time_string = content.find(iden_end_time)
        old_time_string = content[start_old_time_string:end_old_time_string]
        new_time_string = iden_start_time+str(time_new)
        content = content.replace(old_time_string,new_time_string)
        with open(specific, "w") as file:
            file.write(content)
    print(specific,new_time_string)


#token_file_location = "C:\\Users\\--\\0code\\00token_github.txt"
token_file_location = "C:\\Users\\--\\00token_github.txt"
with open(token_file_location, 'r') as file:
    token = file.read()
repo_path = r'C:\Users\--\0stocks'
github_username = 'violin788'
git_user_email = 'violin78@protonmail.com'
github_token = token
repo_name = "stocks"
def run_git_command(command, repo_path):
    try:
        subprocess.run(command, cwd=repo_path, check=True, shell=True)
        print(f"Successfully ran: {' '.join(command)}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}\n{e}")
        exit(1)
def update_github_repo(repo_path, commit_message):
    os.chdir(repo_path)
    subprocess.run(['git', 'config', '--global', 'user.name', github_username], cwd=repo_path, check=True)
    subprocess.run(['git', 'config', '--global', 'user.email', git_user_email], cwd=repo_path, check=True)
    run_git_command(['git', 'add', '.'], repo_path)
    run_git_command(['git', 'commit', '-m', commit_message], repo_path)
    push_command = f"git push https://{github_username}:{github_token}@github.com/{github_username}/"+repo_name+".git main"
    subprocess.run(push_command, cwd=repo_path, shell=True, check=True)
    print("Changes pushed to GitHub successfully.")
commit_message = "updated from laptop to repo"
update_github_repo(repo_path, commit_message)

