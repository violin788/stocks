import subprocess
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

command = f"""
git add .
git commit -m "updated: {time_new}"
git push origin main
"""
result = subprocess.run(command, shell=True, text=True, capture_output=True)
# Print the output of the command
print(result.stdout)



"""
import subprocess
import os

# Path to your local repository
repo_path = "/path/to/your/repo"  # Replace with your repo path

# Function to run git commands
def run_git_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=repo_path)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)

# Run git commands
def git_push():
    run_git_command(['git', 'add', '.'])  # Adds all changes
    run_git_command(['git', 'commit', '-m', 'Updated files in Codespace'])  # Commits changes
    run_git_command(['git', 'push', 'origin', 'main'])  # Pushes to the 'main' branch

if __name__ == '__main__':
    git_push()


"""