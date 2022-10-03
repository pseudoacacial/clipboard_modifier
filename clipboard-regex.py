import pyperclip as pc
import re
while (True):
    clipboard=pc.waitForNewPaste(timeout=None)
    regex = re.search("(?:(border-radius:\s*\d+px;)[\s\S]*)?(left:\s*\d+px;\s*top:\s*\d+px;\s*width:\s*\d+px;\s*height:\s*\d+px;)\s*", clipboard)
    if regex:
        if(regex.group(1)):
            newClipboard = '\n'.join(regex.groups()).strip()
        else:
            newClipboard = regex.group().strip()
        print(newClipboard)
        pc.copy(newClipboard)
