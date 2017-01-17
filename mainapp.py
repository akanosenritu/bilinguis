import ui
import bilinguis


class App(object):
    def __init__(self):
        self.app()

    def app(self):
        ui.load_view("menu").present()



class Practice (object):
    def __init__(self, pairs=[], options=[]):
        pass
        #self.setup(pairs)

    def setup(self, pairs, options):
        self.pairs = pairs
        for option in options:
            if option == "random":
                self.pairs.randomize()
            elif option == "reverse":
                self.pairs.reverse()
        self.current = pairs[0]

    def button_next(self):
        pass

    def button_back(self):
        pass

class PracticeUI:
    @staticmethod
    def button_next(sender):
        pass
        '''
        v = sender.superview
        if v['label2'] == '':
            v['label2'] = app.current[1]
        else:
            app.next()
            v['label1'] = app.current[0]
            v['label2'] = ''

    @staticmethod
    def button2_back(sender):
        v = sender.superview
        if v['label2'] == '':
            v['label2'] = app.current[1]
        else:
            app.next()
            v['label1'] = app.current[0]
            v['label2'] = ''
        '''
        
p = Practice()
ui.load_view('practice').present()
