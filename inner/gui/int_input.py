import tkinter
from tkinter import ttk

class IntInput:
    __slots__ = (
        '__frame',
        '__text',
        '__value',
        '__spinBox'
    )

    def __init__(self, root, text:str, anchor=tkinter.NW, side=tkinter.TOP, initValue=0):
        self.__frame = ttk.Frame(root)
        self.__text = ttk.Label(self.__frame, text=text)
        self.__value = tkinter.IntVar(self.__frame, value=initValue)

        self.__spinBox = ttk.Spinbox(
            self.__frame,
            textvariable=self.__value,
            from_=1,
            to=256,
        )

        self.__text.pack(padx=5, pady=5, side=tkinter.LEFT)
        self.__spinBox.pack(padx=5, pady=5, side=tkinter.RIGHT)
        self.__frame.pack(anchor=anchor, side=side)

    def GetValue(self) -> int:
        return self.__value.get()