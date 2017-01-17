import ui
import bilinguis

class App (object):
    def __init__(self):
        self.setup()

    def setup(self, pairs):
        self.current = Pair(*pairs[0])
        self.count = 0
        self.pairs = pairs
        self.processed = []

    def next(self):
        self.processed.append(self.current)
        self.count += 1
        self.current = Pair(*pairs[i])


def button_next(sender):
    v = sender.superview
    if v['label2'] == '':
        v['label2'] = app.current[1]
    else:
        app.next()
        v['label1'] = app.current[0]
        v['label2'] = ''
        
def button2_back(sender):
    v = sender.superview
    if v['label2'] == '':
        v['label2'] = app.current[1]
    else:
        app.next()
        v['label1'] = app.current[0]
        v['label2'] = ''
        
        
app = App()
ui.load_view('turkish').present('fullscreen')
