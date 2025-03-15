import subprocess
# Example command to run in the terminal
#command = "ls"  # List directory contents (replace with any terminal command)
command = """
git reset --hard
git fetch --all
git reset --hard origin/main
git status
"""
result = subprocess.run(command, shell=True, text=True, capture_output=True)
# Print the output of the command
print(result.stdout)