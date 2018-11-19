#import json
import tkinter
import sys
from search import search

DEFAULT_FONT = ('Verdana', 12)


class NameDialog:
    def __init__(self):
        self.dialog_window = tkinter.Toplevel()
        self.dialog_window.geometry("600x300")
        self.dialog_window.title("CS 121 - Information Retrieval")

        query_label = tkinter.Label( master=self.dialog_window,
                                     text='Search:',
                                     font=('Verdana', 20))

        query_label.grid(
            row=3, column=0, columnspan=1, padx=10, pady=10,
            sticky=tkinter.W + tkinter.E)

        self._query_entry = tkinter.Entry(
            master=self.dialog_window, width=10, font=DEFAULT_FONT)

        self._query_entry.grid(
            row=3, column=1, columnspan=10, padx=10, pady=1,
            sticky=tkinter.W + tkinter.E)

        button_frame = tkinter.Frame(master=self.dialog_window)

        button_frame.grid(
            row=6, column=1, padx=10, pady=10,
            sticky=tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
           master=button_frame, text='OK', font=DEFAULT_FONT,
           command=self._on_ok_button)

        ok_button.grid(
            row=10, column=0, padx=10, pady=10)

        cancel_button = tkinter.Button(
            master=button_frame, text='CANCEL', font=DEFAULT_FONT,
            command=self._on_cancel_button)

        cancel_button.grid(
            row=10, column=1, padx=10, pady=10)

        self.dialog_window.rowconfigure(10, weight=2)
        self.dialog_window.columnconfigure(10, weight=2)
        self.dialog_window.config(height=600, width=300)
        self._ok_clicked = False
        self._query = ''

    def show(self):
        self.dialog_window.grab_set()
        self.dialog_window.wait_window()

    def was_ok_clicked(self):
        return self._ok_clicked

    def get_query(self):
        return self._query

    def _on_ok_button(self):
        self._ok_clicked = True
        self._query = self._query_entry.get()
        self.dialog_window.destroy()

    def _on_cancel_button(self):
        self.dialog_window.destroy()
        sys.exit(0)


class IntroApp:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.withdraw()
        self.on_intro()
        self._query = ''

    def start(self):
        self.root_window.mainloop()

    def on_intro(self):
        dialog = NameDialog()
        dialog.show()
        self.root_window.destroy()

        if dialog.was_ok_clicked():
            self._query = dialog.get_query()
            results = search(self._query)
            if len(results) != 0:
                for x, url in results.items():
                    print(url)
            else:
                print("No results for that search found.")



if __name__ == '__main__':
    while True:
        IntroApp().start()