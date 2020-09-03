import os
import re
import subprocess
import platform

# Checking the operating system
# Also provide the correct Macros
if os.name == 'posix':
    ape = './ape.exe'
elif os.name == 'nt':
    ape = 'ape.exe'

# Takes the text from nl.txt (stands for natural language) and output to text.txt
if __name__ == "__main__":
    file = open("text.owl", "w")
    command = subprocess.run([ape, '-file', 'nl.txt', '-solo', 'owlxml', '-guess'], stdout=file)
