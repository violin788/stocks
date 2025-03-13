import subprocess
# Example command to run in the terminal
#command = "ls"  # List directory contents (replace with any terminal command)
command = """
git add .
git commit -m "Updated files in Codespace"
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