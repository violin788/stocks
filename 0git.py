


#download all of a github repo
#git clone https://github.com/violin788/stocks.git

#update files to github repo from desktop
#just get the command that you use on codespaces
#to push the chnages to the repo?

import subprocess
# Example command to run in the terminal
#command = "ls"  # List directory contents (replace with any terminal command)
command = """
git status
git add .
git commit -m "Your commit message"
git push origin main
"""
result = subprocess.run(command, shell=True, text=True, capture_output=True)
# Print the output of the command
print(result.stdout)


"""
or these below?
git add .
git commit -m "Updated files in Codespace"
git push origin main

meow meow
"""