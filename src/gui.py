# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox
import tkSimpleDialog, pickle

class info_gui():
    def __init__(self, root):
        self.infos = []
        
        root.title("USS Infosystem")
        
        self.btn1 = Tkinter.Button(root, text="Neue Information", command=self.add_info)
        self.btn1.pack(fill='x')

        self.btn2 = Tkinter.Button(root, text="Lösche Information", command=self.delete_info)
        self.btn2.pack(fill='x')

        self.btn3 = Tkinter.Button(root, text="Lösche alle Information", command=self.delete_all_infos)
        self.btn3.pack(fill='x')

        self.btn4 = Tkinter.Button(root, text="Ändere Information", command=self.change_info)
        self.btn4.pack(fill='x')

        self.btn4 = Tkinter.Button(root, text="Zeige Information", command=self.show_content)
        self.btn4.pack(fill='x')

        self.btn4 = Tkinter.Button(root, text="Speichere Informationen", command=self.save)
        self.btn4.pack(fill='x')

        self.btn10 = Tkinter.Button(root, text="Zeige Informationen", command=self.show_infos)
        self.btn10.pack(fill='x')

    def load(self):
        try:
            f = open("data/infos.ussinfos", "rb")
            self.infos = pickle.load(f)
            f.close()
        except:
            tkMessageBox.showinfo("Warnung", "Die Datei data/infos.ussinfos existiert nicht!")

    def save(self):
        f = open("data/infos.ussinfos", "wb")
        pickle.dump(self.infos, f)
        f.close()

    def add_info(self):
        t = tkSimpleDialog.askstring("Neue Information", "Titel")
        c = tkSimpleDialog.askstring("Neue Information", "Inhalt")
        if t and c:
            self.infos.append([t, c])

    def delete_info(self):
        tkMessageBox.showinfo("Fehler XD", "ERROR ID : 82713, Beschreibung : Programmierer war zu faul!")

    def delete_all_infos(self):
        self.infos = []

    def show_infos(self):
        s = ""
        for i in self.infos:
            s += i[0] + "\n"
        tkMessageBox.showinfo("Informationen", s)

    def show_content(self):
        t = tkSimpleDialog.askstring("Zeige Information", "Titel")
        if t:
            for i in range(0, len(self.infos)):
                if self.infos[i][0] == t:
                    tkMessageBox.showinfo("Zeige Information", self.infos[i][1])

    def change_info(self):
        t = tkSimpleDialog.askstring("Ändere Information", "Titel")
        if t:
            for i in range(0, len(self.infos)):
                if self.infos[i][0] == t:
                    self.infos[i][1] = tkSimpleDialog.askstring("Ändere Information", "Inhalt") or " - "
        
    
r = Tkinter.Tk()
i = info_gui(r)
i.load()
r.mainloop()
