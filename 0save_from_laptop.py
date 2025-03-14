import subprocess
import os
repo_path = r'C:\Users\--\code\stocks'
github_username = 'violin788'
github_token = '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'
git_user_name = 'violin788'
git_user_email = 'violin78@protonmail.com'
def run_git_command(command, repo_path):
    try:
        subprocess.run(command, cwd=repo_path, check=True, shell=True)
        print(f"Successfully ran: {' '.join(command)}")
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}\n{e}")
        exit(1)
def update_github_repo(repo_path, commit_message):
    os.chdir(repo_path)
    subprocess.run(['git', 'config', '--global', 'user.name', git_user_name], cwd=repo_path, check=True)
    subprocess.run(['git', 'config', '--global', 'user.email', git_user_email], cwd=repo_path, check=True)
    run_git_command(['git', 'add', '.'], repo_path)
    run_git_command(['git', 'commit', '-m', commit_message], repo_path)
    push_command = f"git push https://{github_username}:{github_token}@github.com/{github_username}/stocks.git main"
    subprocess.run(push_command, cwd=repo_path, shell=True, check=True)
    print("Changes pushed to GitHub successfully.")
commit_message = "Your commit message here"
update_github_repo(repo_path, commit_message)

