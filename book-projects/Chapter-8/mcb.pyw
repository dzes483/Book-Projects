#!/usr/bin/python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
#       py.exe mcb.pyw delete <keyword> - Deletes keyword in mcb_shelf.
#       py.exe mcb.pyw <keyword> - Loads keyword to clipboard
#       py.exe mcb.pyw list - Loads all keywords to clipboard
#       pw.exe mcb.pyw delete - Deletes all keywords

import shelve
import sys
from tkinter import Tk

mcb_shelf = shelve.open('mcb')
type(mcb_shelf)
r = Tk()

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = str(r.selection_get(selection = "CLIPBOARD"))
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcb_shelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        r.clipboard_append(str(list(mcb_shelf.keys())))
        r.mainloop()
        r.after(3000, r.destroy)
    elif sys.argv[1].lower() == 'delete':
        mcb_shelf.clear()
    elif sys.argv[1] in mcb_shelf:
        r.clipboard_append(mcb_shelf[sys.argv[1]])
        r.mainloop()
        r.after(3000, r.destroy)

# Close the file
mcb_shelf.close()
