import ui
import os
import bilinguis


class Menu(object):
    def __init__(self):
        self.view = ui.load_view("menu")
        self.lesson_file = ""
        self.pairs = []
        self.options = {"random":False, "reverse":False}
        self.lesson_files = [file for file in os.listdir("files/") if file.endswith(".txt")]
        self.table_view = self.view["table_view"]
        self.table_view.data_source = self.table_view.delegate = ui.ListDataSource(self.lesson_files)
        self.table_view.delegate.action = self.set_lesson_file
        self.table_view.delete_enabled = False
        self.table_view.reload_data()
        #self.app()
        self.view.present()

    def set_lesson_file(self):
        index = self.table_view.data_source.selected_row
        self.lesson_file = self.lesson_files[index]
        self.pairs = bilinguis.FileBase(self.lesson_file, "files/").parse_content().pairs

    def switch_random(self, sender):
        if sender.value:
            self.options["random"] = True
        else:
            self.options["random"] = False

    def switch_reverse(self, sender):
        if sender.value:
            self.options["reverse"] = True
        else:
            self.options["reverse"] = False

    def button_go(self, sender):
        Practice(bilinguis.Pairs(self.pairs), self.options)

    def button_cancel(self, sender):
        Menu()


class Practice (object):
    def __init__(self, pairs=[], options={}):
        self.view = ui.load_view("practice")
        self.pairs = pairs
        self.count = 0

        for k, v in options.items():
            if v:
                try:
                    exec("self.pairs." + str(k) + "()")
                except AttributeError or TypeError:
                    pass

        self.current = self.pairs.pairs[0]
        self.view.present()

    def next(self):
        self.count += 1
        self.current = self.pairs.pairs[self.count]

    def back(self):
        self.count -= 1
        self.current = self.pairs.pairs[self.count]

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
