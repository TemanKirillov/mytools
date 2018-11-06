#!/usr/bin/python3
import code
import contextlib

class ListIO:
    def __init__(self):
        self.data = []
    def write(self, data):
        self.data.append(data)
    def return_all(self):
        string = ''.join(self.data)
        self.data = []
        return string

class MyInter(code.InteractiveInterpreter):
    def run(self, source):
        lio = ListIO()
        with contextlib.redirect_stdout(lio), contextlib.redirect_stderr(lio):
            ans = self.runsource(source)
        return lio.return_all()

def test():
    fmt = '>>> {}'
    inter = MyInter()
    commands = ['a = 5', 'a', 'a += 10', 'a', 'i']
    for command in commands:
        print(fmt.format(command))
        print(inter.run(command), end='')


if __name__ == '__main__':
    test()
