import pyperclip as pc
from os import system, name
import re

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux
    else:
        _ = system('clear')

while (True):
    clipboard=pc.waitForNewPaste(timeout=None)
    regex = re.search("(?:(border-radius:\s*\d+px;)[\s\S]*)?(left:\s*\d+px;\s*top:\s*\d+px;\s*width:\s*\d+px;\s*height:\s*\d+px;)\s*", clipboard)
    if regex:
        if(regex.group(1)):
            clipboard = '\n'.join(regex.groups())
        else:
            clipboard = regex.group()
        clipboard = '\n'.join(' '.join(line.split()) for line in clipboard.split('\n')).strip()
        pc.copy(clipboard)
    clear()
    print(clipboard)
