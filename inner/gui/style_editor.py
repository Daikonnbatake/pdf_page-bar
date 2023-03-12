import tkinter
from tkinter import ttk

from inner.gui.int_input import IntInput


class StyleEditor:

    __slots__ = (
        '__frame',
        '__barHeight',
        '__barPadding'
    )

    def __init__(self, root):

        self.__frame = ttk.LabelFrame(root, text=u'スタイル設定')

        self.__barHeight = IntInput(
            self.__frame,
            'バーの幅(px)',
            side=tkinter.LEFT,
            initValue=20
        )

        self.__barPadding = IntInput(
            self.__frame,
            'バー下部の余白(px)',
            side=tkinter.RIGHT,
            initValue=0
        )

        self.__frame.pack(padx=5, pady=5, anchor=tkinter.NW)


    def getHeight(self) -> int:
        return self.__barHeight.GetValue()


    def getPadding(self) -> int:
        return self.__barPadding.GetValue()