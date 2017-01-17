import ui
import os
import bilinguis


class Menu(object):
    def __init__(self):
        self.view = ui.load_view("menu")
        self.lesson_files = [file for file in os.listdir("files/") if file.endswith(".txt")]
        self.table_view = self.view["table_view"]
        self.table_view.data_source = self.table_view.delegate = ui.ListDataSource(self.lesson_files)
        self.table_view.delete_enabled = False
        self.table_view.reload_data()
        #self.app()

    def app(self):
        pass

    def button_go(self, sender):
        pass


class Practice (object):
    def __init__(self, pairs=[], options=[]):
        self.pairs = pairs
        self.count = 0
        self.current = []
        self.setup(self.pairs, options)

    def setup(self, pairs, options):
        self.pairs = pairs
        for option in options:
            if option == "random":
                self.pairs.randomize()
            elif option == "reverse":
                self.pairs.reverse()
        self.current = pairs[0]

    def next(self):
        self.count += 1
        self.current = self.pairs[self.count]

    def back(self):
        self.count -= 1
        self.current = self.pairs[self.count]

    def button_next(self, sender):
        v = sender.superview
        if v['label2'] == '':
            v['label2'] = self.current[1]
        else:
            self.next()
            v['label1'] = self.current[0]
            v['label2'] = ''

    def button_back(self, sender):
        v = sender.superview
        if v['label2'] != '':
            v['label2'] = ''
        else:
            self.back()
            v['label1'] = self.current[0]
            v['label2'] = self.current[1]

menu = Menu()
