import os
import tkinter
from tkinter import ttk
from tkinter import messagebox

from inner.dialogs import GetOutPath
from inner.pdf.reader import PDFReader
from inner.pdf.writer import PDFWriter
from inner.gui.path_selector import PathSelector
from inner.gui.style_editor import StyleEditor

class MainWindow:

    __slots__ = (
        '__root',
        '__pathSelector',
        '__styleEditor',
        '__processingButton'
    )

    def __init__(self):
        self.__root = tkinter.Tk()
        self.__root.title(u'pdf page bar')
        self.__root.geometry('450x200')

        self.__pathSelector = PathSelector(self.__root, 'PDF', '*.pdf', '%UserProfile%')
        self.__styleEditor = StyleEditor(self.__root)

        self.__processingButton = ttk.Button(
            self.__root,
            text=u'出力',
            command=self.__save
        )

        self.__processingButton.pack(padx=5, pady=5, side=tkinter.BOTTOM, anchor=tkinter.SE)

    def start(self):
        self.__root.mainloop()

    def __save(self):
        out_path = GetOutPath('PDF', '*.pdf', '%UserProfile%')
        in_path  = self.__pathSelector.getPath()

        barHeight  = self.__styleEditor.getHeight()
        barPadding = self.__styleEditor.getPadding()

        if (not os.path.exists(in_path)):
            messagebox.showerror(
                title=u'無効なパス',
                message=u'ああ、弟よ、君を泣く、\n無効なパスを指定したまふことなかれ.'
            )
            return

        if (barHeight < 1):
            messagebox.showerror(
                title=u'無効な高さ',
                message=u'ああ、弟よ、君を泣く、\n0以下の数値を指定したまふことなかれ.'
            )
            return


        reader = PDFReader(in_path)
        writer = PDFWriter(out_path)

        page_count = reader.getPageCount()

        for i in range(page_count):
            xobj = reader.getPageXOBJ(i)
            writer.doFormXOBJ(xobj)

            page_width, page_height = reader.getPageSize(i)
            length = (page_width / (page_count-1)) * i

            writer.setPageSize(page_width, page_height)

            writer.setFillColor(88, 88, 88)
            writer.rect(0, barPadding, page_width, barHeight, stroke=0, fill=1)

            writer.setFillColor(168, 168, 168)
            writer.rect(0, barPadding, length, barHeight, stroke=0, fill=1)

            writer.flush()

        writer.save()