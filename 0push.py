token = "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"
import requests
repo_owner = 'violin788'  
repo_name = 'stocks'  
branch = 'main'
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents'
def list_files_in_repo(url):
    response = requests.get(url)
    if response.status_code == 200:
        files = response.json()
        for file in files:
            if file['type'] == 'file':
                last_updated = file['last_modified'] if 'last_modified' in file else 'N/A'
                print(f"{file['name']} - Last Updated: {last_updated}")
            elif file['type'] == 'dir':
                list_files_in_repo(file['url'])
    else:
        print(f"Error: {response.status_code}, {response.text}")
    return files

cwd = os.getcwd()
in_codespaces = os.listdir(cwd)
in_repo = list_files_in_repo(url)
in_repo2 = []
for check in in_repo:
    in_repo2.append(check["name"])
print(in_repo2)
for check in in_codespaces:
    if check not in in_repo2:



#for check in in_codespaces:
#    if check not in in_codespaces:

print(in_codespaces)
#print(cwd)
#for file in in_repo:
#    print(file)



"""
def run_git_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=repo_path)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
def file_exists_in_repo():
    result = subprocess.run(['git', 'ls-tree', 'HEAD', '--name-only', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, cwd=repo_path)
    return result.returncode == 0 and file_path in result.stdout
def stage_commit_push():
    run_git_command(['git', 'add', file_path])
    run_git_command(['git', 'commit', '-m', 'Update file from Codespace'])
    run_git_command(['git', 'push'])
def delete_file_from_repo():
    run_git_command(['git', 'rm', file_path])
    run_git_command(['git', 'commit', '-m', 'Delete file from Codespace'])
    run_git_command(['git', 'push'])
if __name__ == '__main__':
    if not os.path.exists(file_path):
        if file_exists_in_repo():
            delete_file_from_repo()
    else:
        if not file_exists_in_repo():
            stage_commit_push()
        else:
            stage_commit_push()
"""