#!/usr/bin/python3

from enum import Enum

class Deco(Enum):
    MID = '├── '
    END = '└── '
    CONT = '│   '
    EMPTY = '    '

class Tree:
    def __init__(self, traverser, print_node, deco=Deco):
        self.deco = deco
        self.traverser = traverser
        self.print_node = print_node

    def print(self):
        for (dstack, node) in self.traverser:
            self._print_decos(dstack)
            self.print_node(node)

    def _print_decos(self, dstack):
        if not dstack:
            return
        for d in dstack[:-1]:
            if d == self.deco.END:
                print(self.deco.EMPTY.value, end='')
            elif d == self.deco.MID:
                print(self.deco.CONT.value, end='')
            else:
                print(d, end='')
        print(dstack[-1].value, end='')
