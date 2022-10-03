import pyperclip as pc
import re
while (True):
    clipboard=pc.waitForNewPaste(timeout=None)
    regex = re.search("left:\s*\d+px;\s*top:\s*\d+px;\s*width:\s*\d+px;\s*height:\s*\d+px;\s*", clipboard)
    if regex:
        newClipboard = regex.group().strip()
        print(newClipboard)
        pc.copy(newClipboard)
