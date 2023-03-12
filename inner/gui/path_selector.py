import os
import tkinter
from tkinter import ttk
from tkinter import filedialog


class PathSelector:

    __slots__ = (
        '__frame',
        '__label',
        '__strVar',
        '__button'
    )

    def __init__(self, root, type: str, wildcard: str, initDir: str):

        self.__frame = ttk.LabelFrame(root, text=u'ファイル選択')
        self.__strVar = tkinter.StringVar(self.__frame)
        self.__strVar.set('ファイルを選択してください')
        self.__label = ttk.Label(self.__frame, textvariable= self.__strVar)

        self.__button = ttk.Button(
            self.__frame,
            text = u'選択',
            command = lambda: self.__strVar.set(PathSelector.__getPath(
                type,
                wildcard,
                initDir,
                self.__strVar.get()
            ))
        )

        self.__button.pack(padx=5, pady=5,side=tkinter.LEFT)
        self.__label.pack(padx=5, pady=5,side=tkinter.RIGHT)
        self.__frame.pack(padx=5, pady=5, anchor=tkinter.NW)


    def getPath(self) -> str:
        return self.__strVar.get()


    @staticmethod
    def __getPath(type: str, wildcard: str, initDir: str, nowValue:str) -> str:
        path = filedialog.askopenfilename(filetypes=[(type, wildcard)], initialdir=initDir)

        if (os.path.exists(path)): return path
        else: return nowValue