import subprocess
# Example command to run in the terminal
#command = "ls"  # List directory contents (replace with any terminal command)
command = """
cd /path/to/your/folder
git clone https://github.com/username/repository.git
cd repository
"""
result = subprocess.run(command, shell=True, text=True, capture_output=True)
# Print the output of the command
print(result.stdout)
