import Tkinter as tk
import tkMessageBox as mbox
from geocode import *

class Hike(Geocode):

    def __init__(self, master):
        Geocode.__init__(self)
        self.master = master
        self.mainframe = tk.Frame(self.master, bg="grey")
        self.mainframe.pack(fill=tk.BOTH, expand=True)
        self.build_grid()
        self.user_input = tk.StringVar()
        self.entry = tk.Entry(
            self.mainframe,
            bd=5,
            textvariable=self.user_input)
        self.entry.grid(
            row=2, column=1,
            columnspan=2,
            sticky='ewns',
            padx=5, pady=5
        )

        self.text_field()
        self.banner()
        self.lang = tk.IntVar()
        self.lang_box()
        self.set_lang()
        self.log_check()
        self.location_text()
        self.submit()
        self.status()
        self.on_button()

    def build_grid(self):
        self.mainframe.columnconfigure(0, weight=1)
        self.mainframe.rowconfigure(1, weight=0)
        self.mainframe.rowconfigure(2, weight=0)
        self.mainframe.rowconfigure(3, weight=0)
        self.mainframe.rowconfigure(4, weight=1)
        self.mainframe.columnconfigure(1, weight=1)




    def banner(self):
        banner = tk.Label(
            self.mainframe,
            text='PyHike',
            fg='red',
            font=('Helvetica', 20)
        )
        banner.grid(
            row=0, columnspan=2,
            sticky='ew',
            padx=10, pady=10
        )


    def lang_box(self):
        box_frame = tk.Frame(self.mainframe)
        box_frame.grid(row=1, column=0, sticky='nsew')
        box_frame.columnconfigure(0, weight=1)
        box_frame.columnconfigure(1, weight=1)
        hu = tk.Radiobutton(
            box_frame,
            text='Hungarian',
            variable=self.lang,
            value=1,
            command=self.set_lang
        )
        hu.grid(
            row=1, column=0,
            columnspan=1,
            sticky='ew',
        )

        en = tk.Radiobutton(
            box_frame,
            text='English',
            variable=self.lang,
            value=2,
            command=self.set_lang
        )
        en.grid(
            row=1, column=1,
            columnspan=1,
            sticky='ew',
        )

    def log_check(self):
        logbox = tk.Checkbutton(
            self.mainframe,
            text="Save log",
        )
        logbox.grid(
            row=1, column=1,
            columnspan=1,
            sticky='ewsn'
        )


    def set_lang(self):
        if self.lang.get() == 1:
            print "Magyar!"
        elif self.lang.get() == 2:
            print "Angol!"


    def location_text(self):
        label = tk.Label(
            self.mainframe,
            text="Enter location:"
        )
        label.grid(
            row=2, column=0,
            columnspan=1,
            sticky='we',
            padx=5, pady=5
        )
    '''
    def entry(self):
        self.entry = tk.Entry(
            self.mainframe,
            bd=5)
        self.entry.grid(
            row=2, column=1,
            columnspan=2,
            sticky='ewns',
            padx=5, pady=5
        )
    '''
    def submit(self):
        button = tk.Button(
            self.mainframe,
            text="Search",
            width=15,
            command=self.search
        )
        button.grid(
            row=3, columnspan=2,
            sticky='wens',
            padx=5, pady=5
        )

    def on_button(self):
        location = self.user_input.get()
        return location

    def search(self):
        self.loc_search(self.on_button())
        self.json_req()
        self.text.delete(1.0, 2.0)
        self.text.insert(1.0, self.geodata()['address'] + '\n')
        self.text.insert(2.0, self.geodata()['id'] + '\n')
        self.text.insert(3.0, self.geodata()['gps'])


    def text_field(self):
        self.text = tk.Text(
            self.mainframe,
            wrap=tk.WORD
        )
        self.text.grid(
            row=4,
            column=0,
            columnspan=2,
            sticky='we'
        )
        self.text.tag_configure('center', justify='center')

    def status(self):
        status = tk.Label(
            self.mainframe,
            text="TEST TEST TES t TE st T est test",
            bd=1,
            relief=tk.SUNKEN
        )
        status.grid(
            row=5,
            columnspan=2,
            sticky='wes'
        )

if __name__ == '__main__':
    root = tk.Tk()
    Hike(root)
    root.mainloop()

