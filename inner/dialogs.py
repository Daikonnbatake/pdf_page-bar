from tkinter import filedialog

def GetInPath(type: str, wildcard: str, initDir: str):
    path = filedialog.askopenfilename(filetypes=[(type, wildcard)], initialdir=initDir)
    return path

def GetOutPath(type: str, wildcard: str, initDir: str):
    path = filedialog.asksaveasfilename(filetypes=[(type, wildcard)], initialdir=initDir)
    return path