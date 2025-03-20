import subprocess
# Example command to run in the terminal
#command = "ls"  # List directory contents (replace with any terminal command)
command = """
git fetch --all  # Fetch latest changes  
git reset --hard origin/main  # Reset local files to match GitHub's main branch  
git pull origin main  # Pull latest files  
"""
subprocess.run(command, shell=True, check=True)


#result = subprocess.run(command, shell=True, text=True, capture_output=True)
# Print the output of the command
#print(result.stdout)

#previous that did not work
"""
git fetch --all  # Fetch latest changes  
git reset --hard origin/main  # Reset local files to match GitHub's main branch  
git pull origin main  # Pull latest files  
"""